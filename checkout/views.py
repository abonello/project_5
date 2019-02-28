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


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET
# stripe.api_key = settings.SECRET_KEY
# print("From view: {}".format(stripe.api_key))

@login_required()
def checkout(request):
    if request.method == "POST":
        print("View received a POST request")
        try:
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)
        except:
            print("Error occured")

        if order_form.is_valid():
            print("Order form is valid")
        else:
            print("Order form is NOT valid")
        if payment_form.is_valid():
            print("Payment form is valid")
        else:
            print("Payment form is NOT valid")

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
                        print("Try getting user ID")
                        user_id = request.user.id
                        print("Getting user ID successful. ID: {}".format(user_id))
                    except:
                        print("Getting user ID FAILED.")

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
                    print(quantity)
                    print("This is the user making the payment:")
                    try:
                        # print(request.user.username)
                        # print(user_id)
                        # print(UserCoins.objects.get(pk = 1))
                        # user_coins = request.user.relateduser.all
                        # print(user_coins)
                        coin_user = request.user.relateduser.all

                        user_coins = get_object_or_404(UserCoins, user=request.user.id)
                        print(user_coins)
                        print(user_coins.coin_amount)
                        print("Add 144")

                        user_coins.coin_amount += 144
                        user_coins.save()
                        print(user_coins.coin_amount)



                        # print(user_coins.coin_amounts)
                        # print(request.user.coin_amount)
                        # user = User.objects.get(email=request.user.email)
                        # { % for coins in user.relateduser.all % }
                        # <p > <strong > Coins < /strong > : {{coins.coin_amount }} < /p >
                        # { % endfor % }
                    except:
                        print("Cannot find USER")
                        # print("Cannot find COIN_AMOUNT")
                    # print(coins)
                    # print(quantity * coins)



                    return redirect(reverse('products'))
                else: 
                    messages.error(request, "Unable to take payment.")
            else:
                print(payment_form.errors)
                messages.error(request, "We were unable to take a payment with that card!")
        except:
            print("Is this where the error is?")
        
    else:
        # Return a blank form
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    
    # time.sleep(25)

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})

