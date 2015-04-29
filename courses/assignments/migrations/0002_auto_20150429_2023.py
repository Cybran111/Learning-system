# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mark',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
