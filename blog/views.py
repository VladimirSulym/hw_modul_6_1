from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Blog
from django.views.generic import ListView, DetailView, UpdateView


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'base.html'

    def get_queryset(self):
        return Blog.objects.filter(active=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset = ...):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'active', 'preview']
    template_name = 'blog_edit.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})