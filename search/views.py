from django.shortcuts import render
from products.models import Product

def do_search(request):
    """Get filtered products based on what 'q' is. """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
