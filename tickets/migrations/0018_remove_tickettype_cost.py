# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_tickettype_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickettype',
            name='cost',
        ),
    ]
