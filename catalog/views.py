from django.http import HttpResponse
from django.shortcuts import render

def catalog(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        return HttpResponse(f"{name}, от Вас получено сообщений")
    return render(request, 'contacts.html')
