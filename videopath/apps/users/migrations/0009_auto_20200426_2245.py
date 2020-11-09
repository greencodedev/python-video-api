# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'u', max_length=1, blank=True, choices=[(b'm', b'male'), (b'f', b'female'), (b'u', b'n/a')]),
        ),
    ]
