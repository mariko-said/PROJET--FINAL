# Generated by Django 4.1.5 on 2023-01-24 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
    ]
