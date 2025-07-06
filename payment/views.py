from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages
from card.Card  import Card
from payment.forms import PostingForm , PaymentForm
from payment.models import PostingAddress ,OrderItem ,Order
from core.models import product
from django.contrib.auth.models import User

# Create your views here.

def process_order(request):
    if request.POST:
        cart = Card(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.totals()
        # get billing info from the billing page
        payment_form = PaymentForm(request.POST or None)

        # get posting session data
        my_posting = request.session.get('my_posting')
        full_name = my_posting['posting_full_name']
        email = my_posting['posting_email']
        posting_address = f"{my_posting['posting_address1']}\n{my_posting['posting_address2']}\n{my_posting['posting_city']}\n{my_posting['posting_state']}\n{my_posting['posting_zipcode']}\n{my_posting['posting_country']}"
        amount_paid = totals

        # create an order
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user , full_name= full_name , email=email , posting_address=posting_address , amount_paid=amount_paid)
            create_order.save()

            # add order items
            # get the order ID
            order_id = create_order.pk
            # get product info
            for product in  cart_products:
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else :
                    price = product.price
                for key , value in quantities.items():
                    if int(key) == product.id:
                        create_order_item = OrderItem( order_fk=create_order, product_fk=product, user=user, quantity=value, price=price)
                        create_order_item.save()

            # delete our cart
            for key in list(request.session.keys()):
                if key == "cart":
                    # Delete the key
                    del request.session[key]

            messages.success(request, "Order Placed")
            return redirect('home')
        else :
            create_order = Order(full_name=full_name, email=email, posting_address=posting_address, amount_paid=amount_paid)
            create_order.save()

            order_id = create_order.pk
            # get product info
            for product in cart_products:
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                for key, value in quantities.items():
                    if int(key) == product.id:
                        create_order_item = OrderItem(order_fk=create_order, product_fk=product,
                                                      quantity=value, price=price)
                        create_order_item.save()

            for key in list(request.session.keys()):
                if key == "cart":
                    # Delete the key
                    del request.session[key]
            messages.success(request, "Order Placed")
            return redirect('home')
    else :
        messages.success(request , "Access Denied")
        return redirect('home')
def billing_info(request):
    if request.POST:
        cart = Card(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.totals()

        # create a session with posting info
        my_posting = request.POST
        request.session['my_posting'] = my_posting
        # check to see if user is logged in
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html', {'cart_products': cart_products,
                                                                 'quantities': quantities,
                                                                 'totals': totals,
                                                                 'posting_info': request.POST,
                                                                 'billing_form': billing_form ,})
        else :
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html', {'cart_products': cart_products, 'quantities': quantities, 'totals': totals, 'posting_info': request.POST, 'billing_form': billing_form ,})
        posting_form = request.POST
        return render(request, 'payment/billing_info.html', {'cart_products': cart_products,
                                                             'quantities': quantities,
                                                             'totals': totals,
                                                             'posting_form': posting_form, })
    else :
        messages.success(request , "Access Denied")
        return redirect('home')

def checkout(request):
    cart = Card(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.totals()
    if request.user.is_authenticated:
        # check out as a logged in
        posting_user = PostingAddress.objects.get(user__id=request.user.id)
        posting_form = PostingForm(request.POST or None, instance=posting_user)
        return render(request, 'payment/checkout.html', {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals ,
            'posting_form' : posting_form ,
        })
    else:
        # check out as a guest
        posting_form = PostingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals ,
            'posting_form': posting_form,
        })
def payment_success(request):
    return render(request , "payment/payment_success.html" , {})

