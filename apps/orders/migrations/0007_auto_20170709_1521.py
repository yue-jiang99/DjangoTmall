# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-09 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_deliveryaddress_order_orderitem_pointlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='pointlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='PointLog',
        ),
    ]
