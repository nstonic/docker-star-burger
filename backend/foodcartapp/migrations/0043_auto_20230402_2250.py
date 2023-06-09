# Generated by Django 3.2.15 on 2023-04-02 18:50
from decimal import Decimal

from django.db import migrations


def add_prices(apps, schema_editor):
    ProductInCart = apps.get_model('foodcartapp', 'ProductInCart')
    for product_in_cart in ProductInCart.objects.iterator():
        product_in_cart.price = Decimal(product_in_cart.product.price)
        product_in_cart.save()


class Migration(migrations.Migration):
    dependencies = [
        ('foodcartapp', '0042_productincart_price'),
    ]

    operations = [
        migrations.RunPython(add_prices)
    ]
