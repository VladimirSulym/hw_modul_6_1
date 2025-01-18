import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class CatalogView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductInfoView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        return HttpResponse(f"{name}, от Вас получено сообщений")


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    # fields = ['name', 'price', 'description', 'category', 'image']
    form_class = ProductForm
    template_name = 'add_product.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('catalog:add_success')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AddSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'add_success.html'


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'del_product.html'
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        if self.request.user == self.object.owner or self.request.user.has_perm('catalog.can_unpublish_product'):
            os.remove(self.object.image.path) if self.object.image else None
            return super().form_valid(form)
        else:
            return HttpResponseForbidden('Вы не владелец и не модератор и не можете удалять этот продукт')


class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        if self.request.user == self.object.owner:
            if not self.request.user.has_perm('catalog.can_unpublish_product') and form.instance.is_active == False:
                return HttpResponseForbidden('Вы не модератор и не можете редактировать статус публикации')
            elif self.request.user.has_perm('catalog.can_unpublish_product') and form.instance.is_active == False:
                return super().form_valid(form)
            else:
                return super().form_valid(form)
        else:
            return HttpResponseForbidden('Вы не владелец и не можете редактировать этот продукт')

    # def post(self, request, *args, **kwargs):
    #     name = request.POST['name']
    #     price = request.POST['price']
    #     description = request.POST['description']
    #     category = request.POST['category']
    #     image = request.FILES.get('image')
    #     Product.objects.create(name=name, price=float(price), description=description,
    #                            category=Category.objects.get(id=category), image=image)
    #     return render(request, 'add_success.html')

# def catalog(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', context={'products': products})


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         phone = request.POST['phone']
#         message = request.POST['message']
#         return HttpResponse(f"{name}, от Вас получено сообщений")
#     return render(request, 'contacts.html')


# def product_info(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return render(request, 'product.html', context={'product': product})


# def add_product(request):
#     categories = Category.objects.all()
#     if request.method == "POST":
#         name = request.POST['name']
#         price = request.POST['price']
#         description = request.POST['description']
#         category = request.POST['category']
#         # image = request.POST['image']
#         image = request.FILES.get('image')
#         Product.objects.create(name=name, price=float(price), description=description,
#                                category=Category.objects.get(id=category), image=image)
#         return render(request, 'add_success.html')
#     return render(request, 'add_product.html', context={'categories': categories})
