# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_me'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Me',
        ),
    ]