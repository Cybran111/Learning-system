# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_auto_20150505_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='questionset',
            name='type',
            field=models.TextField(default='multiset', choices=[(b'multiset', b'Multiple checkboxes'), (b'singleset', b'Radiobuttons'), (b'multiset_custom', b"Multiple checkboxes with student's own answer"), (b'singleset_custom', b"Radiobuttons with student's own answer")]),
            preserve_default=False,
        ),
    ]
