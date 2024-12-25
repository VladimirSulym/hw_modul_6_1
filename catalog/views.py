from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Category


def catalog(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={'products': products})


def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        return HttpResponse(f"{name}, от Вас получено сообщений")
    return render(request, 'contacts.html')


def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', context={'product': product})


def add_product(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        category = request.POST['category']
        # image = request.POST['image']
        image = request.FILES.get('image')
        Product.objects.create(name=name, price=float(price), description=description,
                               category=Category.objects.get(id=category), image = image)
        return render(request, 'add_success.html')
    return render(request, 'add_product.html', context={'categories': categories})
