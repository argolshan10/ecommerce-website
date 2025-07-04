from django.shortcuts import render
from card.Card  import Card
from payment.forms import PostingForm
from payment.models import PostingAddress


# Create your views here.
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

