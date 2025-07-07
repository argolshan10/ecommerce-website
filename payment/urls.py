from django.urls import path
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info' , views.billing_info , name='billing_info') ,
    path('process_order' , views.process_order , name= 'process_order') ,
    path('posted_dash' , views.posted_dash , name= 'posted_dash') ,
    path('not_posted_dash' , views.not_posted_dash , name= 'not_posted_dash') ,
    path('orders/<int:pk>' , views.orders , name= 'orders') ,
]

