# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ref',
            field=models.CharField(max_length=16, blank=True),
        ),
    ]
