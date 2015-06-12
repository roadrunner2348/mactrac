# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_defaults(apps, schema_editor):
    Status = apps.get_model("inventory", "Status")
    default_status = Status(id=1,name="Active", checkedout=True)
    default_status.save()
    default_status = Status(id=2,name="Retired", checkedout=False)
    default_status.save()

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_status_checkedout'),
    ]

    operations = [
    	migrations.RunPython(load_defaults, reverse_code=migrations.RunPython.noop)
    ]
