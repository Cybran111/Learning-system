# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):
    dependencies = []

    operations = [migrations.CreateModel(name='Course',
        fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(unique=True)),
                ('img', models.ImageField(default=b'../media/courses/default.png', upload_to=b'courses')),
                ('short_description', models.TextField(default=b'')),
                ('full_description', models.TextField(default=b'')), ], options={}, bases=(models.Model,), ),
                  migrations.CreateModel(name='Lecture', fields=[
                      ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                      ('order_id', models.IntegerField()), ('title', models.CharField(max_length=80)), ('video_url',
                                                                                                        models.URLField(
                                                                                                            validators=[
                                                                                                                django.core.validators.RegexValidator(
                                                                                                                    b'^https?:\\/\\/(www\\.)?youtube\\.com\\/watch\\?v\\=\\S{11}$',
                                                                                                                    b'It is not from Youtube')])),
                      ('embed_video_url', models.URLField(validators=[django.core.validators.RegexValidator(
                          b'^https?:\\/\\/(www\\.)?youtube\\.com\\/embed\\/\\S{11}$', b'Something bad with URL')])), ],
                      options={}, bases=(models.Model,), ), migrations.CreateModel(name='Week',
            fields=[('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('number', models.IntegerField(verbose_name=b'Number of week')),
                    ('course', models.ForeignKey(to='courses.Course')), ], options={}, bases=(models.Model,), ),
                  migrations.AlterUniqueTogether(name='week', unique_together=set([('course', 'number')]), ),
                  migrations.AddField(model_name='lecture', name='week', field=models.ForeignKey(to='courses.Week'),
                      preserve_default=True, ),
                  migrations.AlterUniqueTogether(name='lecture', unique_together=set([('order_id', 'week')]), ), ]
