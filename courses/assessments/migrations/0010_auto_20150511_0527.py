# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0009_auto_20150508_0941'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='possibleanswer',
            unique_together=set([('question', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('questionset', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='questionset',
            unique_together=set([('number', 'course', 'week', 'title')]),
        ),
    ]
