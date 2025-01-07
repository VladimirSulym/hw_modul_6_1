import os

from django.urls import reverse_lazy

from .models import Blog
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
from django.views.generic.edit import CreateView

from django.core.mail import send_mail


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'base.html'

    def get_queryset(self):
        return Blog.objects.filter(active=True)

    def get_context_object_name(self, object_list):
        for obj in object_list:
            print ('путь к изображению:', obj.preview if obj.preview else 'Нет изображения')
        return super().get_context_object_name(object_list)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset = ...):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        if obj.views == 100:
            send_mail(
                'Повышенное число просмотров',
                f'ПОЗДРАВЛЯЮ!! Блог {obj.title} просмотрен 100 раз!!',
                'vormagic@yandex.ru',
                ['vormagic@yandex.ru'],
                fail_silently=False,
            )
        return obj

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'active', 'preview']
    template_name = 'blog_edit.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'active']
    template_name = 'add_blog.html'
    context_object_name = 'blogs'
    success_url = reverse_lazy('blog:add_blog_success')

class AddBlogSuccessView(TemplateView):
    template_name = 'add_blog_success.html'

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_context_object_name(self, obj):
        print ('путь к изображению:', obj.preview if obj.preview else 'Нет изображения')
        os.remove(obj.preview.path) if obj.preview else None
        return super().get_context_object_name(obj)