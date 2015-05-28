# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150513_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=100, verbose_name=b'img'),
        ),
    ]
