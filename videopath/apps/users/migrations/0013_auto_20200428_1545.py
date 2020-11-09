# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200428_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='industry',
            field=models.IntegerField(default=1),
        ),
    ]
