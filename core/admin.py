from django.contrib import admin
from .models import category , product , order , customer , Profile
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(category) 
admin.site.register(product)
admin.site.register(order)
admin.site.register(customer)
admin.site.register(Profile)

# mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username" , "first_name" , "last_name" , "email"]
    inlines = [ProfileInline]

# unregister in the old way
admin.site.unregister(User)

# re-register the new way
admin.site.register(User , UserAdmin)
