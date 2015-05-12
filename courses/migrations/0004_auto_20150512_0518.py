# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lecturematerials'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ('order_id',)},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('date_created',)},
        ),
    ]
