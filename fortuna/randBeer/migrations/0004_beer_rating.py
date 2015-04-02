# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randBeer', '0003_auto_20150402_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='rating',
            field=models.IntegerField(default=2.5),
            preserve_default=True,
        ),
    ]
