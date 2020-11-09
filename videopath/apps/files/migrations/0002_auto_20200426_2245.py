# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image_type',
            field=models.CharField(default=b'marker content', max_length=255, blank=True, choices=[(b'marker content', b'Image for Marker Content'), (b'custom thumbnail', b'Image for custom video thumbnail'), (b'custom logo', b'Image for custom logo on player chrome'), (b'profile avatar', b'Profile avatar')]),
        ),
    ]
