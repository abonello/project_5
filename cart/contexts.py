from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering 
    every page.
    """

    # request the cart from session if there is one
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    coin_total = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        coin_total = quantity * 500
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'coin_total': coin_total})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'coin_total': coin_total}