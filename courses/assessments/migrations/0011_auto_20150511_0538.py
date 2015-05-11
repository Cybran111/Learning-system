# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0010_auto_20150511_0527'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='possibleanswer',
            unique_together=set([('question', 'number'), ('question', 'text')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('questionset', 'number'), ('questionset', 'text')]),
        ),
        migrations.AlterUniqueTogether(
            name='studentanswer',
            unique_together=set([('answerset', 'question', 'chosed_answer')]),
        ),
        migrations.AlterUniqueTogether(
            name='studentanswerset',
            unique_together=set([('user', 'number', 'questionset')]),
        ),
    ]
