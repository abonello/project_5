from django.shortcuts import render
from .models import Product

def all_products(request):
    """Get all products"""
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
