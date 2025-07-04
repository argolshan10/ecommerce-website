from django.shortcuts import render , get_object_or_404
from .Card import Card 
from core.models import product 
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


def card_summary(request):
    cart = Card(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.totals()

    return render(request, 'card_summary.html', {
        'cart_products': cart_products,
        'quantities': quantities ,
        'totals': totals
    })


def add(request):
    # get the card 
    cart = Card(request)
    # test for post 
    if request.POST.get('action') == 'post' : 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))  
        # look up products in DB 
        product_obj = get_object_or_404(product , id = product_id)  
    
        # save to session 
        cart.add(product=product_obj , quantity=product_qty) 
        
        # get cart quantity
        cart_quantity = cart.__len__() 
        # return response 
        response = JsonResponse({ 'qty' : cart_quantity})
        messages.success(request, "product added successfully")
        return response 

def delete(request):
    cart = Card(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, "product was deleted successfully")
        return response

def update(request):
    cart = Card(request)
    if request.POST.get('action') == 'post' :
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(our_product=product_id , quantity=product_qty)

        response = JsonResponse({'qty' : product_qty})
        messages.success(request, "Your cart has been updated.")
        return response