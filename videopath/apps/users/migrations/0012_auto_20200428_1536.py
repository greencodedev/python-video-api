# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200426_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='industry',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='industry_other',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ForeignKey(related_name='avatar_thumbnail', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='files.ImageFile', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'u', max_length=1, choices=[(b'u', b'n/a'), (b'm', b'male'), (b'f', b'female')]),
        ),
    ]
