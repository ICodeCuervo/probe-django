# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=20, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='id_category',
            field=models.ForeignKey(db_column='id_category', default=None, on_delete=django.db.models.deletion.CASCADE, to='post.Category'),
        ),
    ]