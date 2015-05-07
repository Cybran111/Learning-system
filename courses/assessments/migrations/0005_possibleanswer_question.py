# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [('assessments', '0004_auto_20150505_0740'), ]

    operations = [migrations.AddField(model_name='possibleanswer', name='question',
        field=models.ForeignKey(default=1, to='assessments.Question'), preserve_default=False, ), ]
