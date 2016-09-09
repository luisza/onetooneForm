# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RelToParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr1', models.SmallIntegerField(default=10)),
                ('attr2', models.SmallIntegerField(default=20)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onetooneForm.Parent')),
            ],
        ),
    ]