# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160314_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
