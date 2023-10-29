# Generated by Django 4.1.7 on 2023-10-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
