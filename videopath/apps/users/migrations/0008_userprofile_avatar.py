# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('users', '0007_userprofile_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ForeignKey(related_name='avatar_thumbnail', default=None, blank=True, to='files.ImageFile', null=True),
        ),
    ]
