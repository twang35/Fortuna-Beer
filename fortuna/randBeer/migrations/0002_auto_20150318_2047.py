# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randBeer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(max_length=50)),
                ('favBeer', models.ForeignKey(to='randBeer.Beer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='beer',
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.AddField(
            model_name='beer',
            name='attr1',
            field=models.CharField(default=b'00000', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='attr2',
            field=models.CharField(default=b'00000', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='val1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='val2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
