# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150429_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureMaterials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('link', models.URLField()),
                ('lecture', models.ForeignKey(to='courses.Lecture')),
            ],
        ),
    ]
