# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20190914_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='This is a note'),
            preserve_default=False,
        ),
    ]
