# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ('courses', '0003_lecturematerials'), ]

    operations = [migrations.CreateModel(name='PossibleAnswer',
        fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()), ('is_correct', models.BooleanField(default=False)),
                ('explanation', models.TextField()), ], ), migrations.CreateModel(name='Question',
        fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()), ('explanation', models.TextField()),
                ('value', models.PositiveIntegerField()), ], ), migrations.CreateModel(name='QuestionSet',
        fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(unique=True)), ('description', models.TextField(unique=True)),
                ('number', models.IntegerField()), ('max_questions', models.PositiveIntegerField()),
                ('course', models.ForeignKey(to='courses.Course')),
                ('week', models.ForeignKey(to='courses.Week')), ], ), migrations.CreateModel(name='StudentAnswer',
        fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)), ], ),
                  migrations.CreateModel(name='StudentAnswerSet', fields=[
                      ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                      ('mark', models.PositiveIntegerField()), ('is_finished', models.BooleanField(default=False)),
                      ('questionset', models.ForeignKey(to='assessments.QuestionSet')),
                      ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)), ], ),
                  migrations.AddField(model_name='studentanswer', name='answerset',
                      field=models.ForeignKey(to='assessments.StudentAnswerSet'), ),
                  migrations.AddField(model_name='studentanswer', name='chosed_answer',
                      field=models.ForeignKey(to='assessments.PossibleAnswer'), ),
                  migrations.AddField(model_name='studentanswer', name='question',
                      field=models.ForeignKey(to='assessments.Question'), ),
                  migrations.AddField(model_name='question', name='questionset',
                      field=models.ForeignKey(to='assessments.QuestionSet'), ), ]
