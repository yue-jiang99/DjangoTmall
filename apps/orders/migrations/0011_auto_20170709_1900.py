# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-09 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_deliveryaddress_order_orderitem_pointlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliver_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发货时间'),
        ),
        migrations.AddField(
            model_name='order',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='收货时间'),
        ),
    ]