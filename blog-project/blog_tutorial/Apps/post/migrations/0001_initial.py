# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 03:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=60, verbose_name='Título del post')),
                ('descr', models.TextField(db_column='descrip', max_length=200, verbose_name='Descripción')),
                ('body', models.TextField(db_column='body', max_length=500, verbose_name='Cuerpo')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Fecha de publicación')),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Post',
                'managed': True,
            },
        ),
    ]
