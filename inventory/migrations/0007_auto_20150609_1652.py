# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150609_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='state_id',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
