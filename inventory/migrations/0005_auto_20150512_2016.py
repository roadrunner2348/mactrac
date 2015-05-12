# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_defaults(apps, schema_editor):
    Program = apps.get_model("inventory", "Program")
    default_program = Program(id=1,name="Unassigned")
    default_program.save()

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150512_2004'),
    ]

    operations = [
    	migrations.RunPython(load_defaults)
    ]
