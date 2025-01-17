# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 22:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message=b'Affinity Group Code can only be digits & letters and min length of 3, max of 7', regex=b'^[a-zA-Z\\d]{3,}$')])),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
