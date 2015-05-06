# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0003_auto_20150505_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possibleanswer',
            name='correct_value',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
