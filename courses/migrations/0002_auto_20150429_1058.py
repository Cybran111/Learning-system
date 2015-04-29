# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default=b'/media/courses/default.png', upload_to=b'courses'),
        ),
        migrations.AddField(
            model_name='news',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
    ]
