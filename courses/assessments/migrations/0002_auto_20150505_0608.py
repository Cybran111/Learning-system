# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='possibleanswer',
            name='correct_value',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.TextField(default='multiset', choices=[(b'multiset', b'Multiple checkboxes'), (b'singleset', b'Radiobuttons'), (b'multiset_custom', b"Multiple checkboxes with student's own answer"), (b'singleset_custom', b"Radiobuttons with student's own answer")]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='possibleanswer',
            name='explanation',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
