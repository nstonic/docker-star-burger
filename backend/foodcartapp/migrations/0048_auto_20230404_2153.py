# Generated by Django 3.2.15 on 2023-04-04 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0047_auto_20230404_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Доставлен'),
        ),
        migrations.AlterField(
            model_name='order',
            name='processed_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Обработан менеджером'),
        ),
    ]