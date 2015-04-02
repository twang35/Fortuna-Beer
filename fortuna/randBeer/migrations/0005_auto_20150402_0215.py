# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('randBeer', '0004_beer_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='attr1',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='attr2',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='val1',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='val2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favBeer',
        ),
        migrations.AddField(
            model_name='beer',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
