# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20200426_2245'),
        ('users', '0016_team_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='team',
            name='cover',
            field=models.ForeignKey(related_name='cover_thumbnail', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='files.ImageFile', null=True),
        ),
    ]
