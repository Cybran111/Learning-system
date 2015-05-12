# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0011_auto_20150511_0538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='possibleanswer',
            options={'ordering': ('number',)},
        ),
        migrations.AlterModelOptions(
            name='questionset',
            options={'ordering': ('number',)},
        ),
    ]
