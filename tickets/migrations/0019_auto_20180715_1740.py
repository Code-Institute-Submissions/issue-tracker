# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0018_remove_tickettype_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='image',
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]