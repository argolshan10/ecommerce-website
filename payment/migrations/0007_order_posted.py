# Generated by Django 5.2 on 2025-07-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_orderitem_order_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='posted',
            field=models.BooleanField(default=False),
        ),
    ]
