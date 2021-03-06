# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0019_auto_20180715_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_ticket_id', models.IntegerField()),
                ('date_started', models.DateTimeField(blank=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
            ],
        ),
    ]
