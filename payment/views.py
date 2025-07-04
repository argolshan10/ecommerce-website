from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages
from card.Card  import Card
from payment.forms import PostingForm , PaymentForm
from payment.models import PostingAddress


# Create your views here.

def billing_info(request):
    if request.POST:
        cart = Card(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.totals()

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

