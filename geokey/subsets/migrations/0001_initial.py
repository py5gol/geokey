# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    from django_pgjson.fields import JsonBField as JSONFieldd
from django.conf import settings
import geokey.core.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150202_1041'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('filters', JSONField(null=True, blank=True)),
                ('where_clause', models.TextField(null=True, blank=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name='subsets', to='projects.Project')),
            ],
            options={
            },
            bases=(geokey.core.mixins.FilterMixin, models.Model),
        ),
    ]
