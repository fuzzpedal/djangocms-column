# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_bootstrap_column', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultiColumns',
            new_name='MultiResponsiveColumns',
        ),
        migrations.RenameModel(
            old_name='Column',
            new_name='ResponsiveColumn',
        ),
    ]
