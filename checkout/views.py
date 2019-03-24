from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from accounts.models import UserCoins
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
import time


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        try:
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)
        except:
            '''Error occured'''
            pass

        try: 
            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.save()

                cart = request.session.get('cart', {})
                total = 0

                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order = order,
                        product = product,
                        quantity = quantity
                        )
                    order_line_item.save()

                try: 
                    # stripe works with cents or pence
                    try:
                        user_id = request.user.id
                    except:
                        '''Getting user ID FAILED'''
                        pass

                    customer = stripe.Charge.create(
                        amount = int(total * 100),
                        currency = "EUR",
                        description = request.user.email,
                        card = payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")

                if customer.paid:
                    messages.error(request, "You have successfully paid.")
                    # Empty cart
                    request.session['cart'] = {}
                    try:
                        user_coins = get_object_or_404(UserCoins, user=request.user.id)
                        coins_to_add = 500 * quantity
                        user_coins.coin_amount += coins_to_add
                        user_coins.save()
                    except:
                        '''Cannot find USER'''
                        pass

                    return redirect(reverse('products'))
                else: 
                    messages.error(request, "Unable to take payment.")
            else:
                messages.error(request, "We were unable to take a payment with that card!")
        except:
            pass
        
    else:
        # Return a blank form
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})