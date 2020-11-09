# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_markercontent_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markercontent',
            name='content',
            field=models.TextField(default=b'{}', null=True, blank=True),
        ),
    ]
