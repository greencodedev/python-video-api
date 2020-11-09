# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20160622_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, blank=True)),
                ('last_name', models.CharField(max_length=64, blank=True)),
                ('phone', models.CharField(max_length=32, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('user', models.OneToOneField(related_name='profile', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profiles',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
