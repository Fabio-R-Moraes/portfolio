from django.shortcuts import render

def index(request):
    return render(request, "portfolio/index.html")

def product(request, id):
    return render(request, 'portfolio/pages/product-view.html', context={
        'nome':'Fábio Rodrigues de Moraes',
    })

def about(request):
    return render(request, 'portfolio/pages/about.html')

def curriculum(request):
    return render(request, 'portfolio/pages/curriculum.html')

def contact(request):
    return render(request, 'portfolio/pages/contact.html')