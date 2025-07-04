from django.contrib import admin
from .models import PostingAddress, Order , OrderItem

# Register your models here.

# register the model on the admin section
admin.site.register(PostingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

