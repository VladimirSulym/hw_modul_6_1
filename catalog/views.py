from django.shortcuts import render

def catalog(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')