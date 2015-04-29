# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_lecturematerials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('checker_url', models.URLField()),
                ('course', models.ForeignKey(to='courses.Course')),
                ('week', models.ForeignKey(to='courses.Week')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attempt', models.PositiveIntegerField()),
                ('mark', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('check_date', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(to='assignments.Assignment')),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together=set([('assignment', 'student', 'attempt')]),
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set([('number', 'course', 'week')]),
        ),
    ]
