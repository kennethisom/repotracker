# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('short_name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=400)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('latest_hash', models.CharField(max_length=30, null=True, blank=True)),
                ('submitting_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['short_name', 'name'],
            },
            bases=(models.Model,),
        ),
    ]
