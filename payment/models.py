from django.db import models
from django.contrib.auth.models import User
from core.models import product
from django.db.models.signals import post_save

# Create your models here.

class PostingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    posting_full_name = models.CharField(max_length=255)
    posting_email = models.CharField(max_length=255)
    posting_address1 = models.CharField(max_length=255)
    posting_address2 = models.CharField(max_length=255)
    posting_city = models.CharField(max_length=255)
    posting_state = models.CharField(max_length=255 , null=True , blank=True)
    posting_zipcode = models.CharField(max_length=255 , null=True , blank=True)
    posting_country = models.CharField(max_length=255)

    # don't pluralize address
    class Meta:
        verbose_name_plural = "Posting Address"

    def __str__(self):
        return f'Posting Address - {str(self.id)}'


def create_posting(sender, instance, created, **kwargs):
    if created:
        user_posting = PostingAddress(user=instance)
        user_posting.save()
post_save.connect(create_posting , sender = User)


# order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    posting_address = models.TextField(max_length=15000)
    amount_paid = models.DecimalField(max_digits=7 , decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'


class OrderItem(models.Model):
    order_fk = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_fk = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Order Item - {str(self.id)}'



