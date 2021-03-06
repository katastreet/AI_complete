# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-01 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('question_class', models.CharField(max_length=200)),
                ('answer', models.IntegerField()),
                ('date', models.DateTimeField(default=None, verbose_name='date asked')),
            ],
        ),
    ]
