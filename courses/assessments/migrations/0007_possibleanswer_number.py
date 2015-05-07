# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [('assessments', '0006_auto_20150506_1420'), ]

    operations = [migrations.AddField(model_name='possibleanswer', name='number', field=models.IntegerField(default=1),
        preserve_default=False, ), ]
