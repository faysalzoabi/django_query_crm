from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('home')
    return render(request, 'accounts/dashboard.html')


def products(request):
    # return HttpResponse('products')
    return render(request, 'accounts/products.html')


def customer(request):
    # return HttpResponse('customer')
    return render(request, 'accounts/Customer.html')
