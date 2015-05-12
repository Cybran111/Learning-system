# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0012_auto_20150512_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionset',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='questionset',
            unique_together=set([('number', 'course', 'week'), ('title', 'week', 'course')]),
        ),
    ]
