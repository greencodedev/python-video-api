# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def replace_teams_title(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Team = apps.get_model('users', 'Team')
    for team in Team.objects.filter(name='My Projects'):
        team.name = 'My Videos'
        team.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200511_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.RunPython(replace_teams_title),
    ]
