# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0008_question_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswerset',
            name='assigned_question',
            field=models.ManyToManyField(to='assessments.Question'),
        ),
        migrations.AddField(
            model_name='studentanswerset',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentanswerset',
            name='mark',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
