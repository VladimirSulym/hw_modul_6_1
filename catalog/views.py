from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product, Category


class CatalogView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductInfoView(DetailView):
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

class AddProductView(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'category', 'image']
    template_name = 'add_product.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('catalog:add_success')

class AddSuccessView(TemplateView):
    template_name = 'add_success.html'


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
