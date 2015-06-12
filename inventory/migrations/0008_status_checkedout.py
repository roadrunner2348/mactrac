# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20150609_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='checkedout',
            field=models.BooleanField(default=False),
        ),
    ]
