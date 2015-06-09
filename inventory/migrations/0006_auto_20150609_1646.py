# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20150512_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='state_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
