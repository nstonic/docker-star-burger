# Generated by Django 4.2 on 2023-04-13 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0055_alter_order_delivered_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivered_at',
            new_name='finished_at',
        ),
    ]
