# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20170420_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]