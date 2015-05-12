# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150512_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.ForeignKey(on_delete=b'SET_DEFAULT', default=b'1', to='inventory.Program'),
        ),
    ]
