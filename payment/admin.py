from django.contrib import admin
from .models import PostingAddress, Order , OrderItem
from django.contrib.auth.models import User
# Register your models here.

# register the model on the admin section
admin.site.register(PostingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# Create an OrderItem Inline
class OrderItemInline(admin.StackedInline):
	model = OrderItem
	extra = 0

# extend order model
class OrderAdmin(admin.ModelAdmin):
	model = Order
	readonly_fields = ["date_ordered"]
	fields = ["user", "full_name", "email", "posting_address", "amount_paid", "date_ordered", "posted" , "date_posted"]
	inlines = [OrderItemInline]

# unregister order model
admin.site.unregister(Order)

# re-register Order and OrderAdmin
admin.site.register(Order, OrderAdmin)