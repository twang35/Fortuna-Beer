# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('randBeer', '0005_auto_20150402_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 6, 46, 42, 520059, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
