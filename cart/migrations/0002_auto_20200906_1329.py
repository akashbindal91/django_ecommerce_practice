# Generated by Django 2.2 on 2020-09-06 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cart_item',
        ),
    ]