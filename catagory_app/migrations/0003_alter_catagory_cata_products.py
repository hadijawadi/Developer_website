# Generated by Django 5.1.3 on 2024-11-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory_app', '0002_alter_catagory_cata_products'),
        ('products_app', '0005_alter_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='cata_products',
            field=models.ManyToManyField(to='products_app.products'),
        ),
    ]
