# Generated by Django 5.1.3 on 2024-12-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_cart_app', '0006_remove_usercart_product_name_usercart_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]