# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20160128_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 1, 28, 17, 47, 28, 298369, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
