# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_organizationpage_twitter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationindexpage',
            options={'verbose_name': 'Practitioner', 'verbose_name_plural': 'Practitioners'},
        ),
    ]