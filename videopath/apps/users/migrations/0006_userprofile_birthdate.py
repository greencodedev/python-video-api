# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
