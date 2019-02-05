from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page."""

    # We do not need to pass a dictionary for the context because
    # the context is available everywhere in its own file.
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart."""
    quantity=int(request.POST.get('quantity'))
    # get a cart that already exists or an empty dictionary
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))

def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount."""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity # IS THIS CORRECT????????????
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
