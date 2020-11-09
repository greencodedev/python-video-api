# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200428_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='industry',
            field=models.IntegerField(default=1, choices=[(1, b'n/a'), (10, b'Aerospace'), (20, b'Agriculture'), (30, b'Computer'), (40, b'Construction'), (50, b'Education'), (60, b'Electronics'), (70, b'Energy'), (80, b'Entertainment'), (90, b'Food'), (100, b'Health care'), (110, b'Hospitality'), (120, b'Manufacturing'), (130, b'Mining'), (140, b'Music'), (150, b'News Media'), (160, b'Pharmaceutical'), (170, b'Telecommunication'), (180, b'Transport'), (190, b'Worldwide web'), (999, b'Other')]),
        ),
    ]
