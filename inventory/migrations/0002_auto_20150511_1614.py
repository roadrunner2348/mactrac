# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade_level',
            field=models.CharField(max_length=2, choices=[(b'3H', b'Half-day Pre-School (3 Years Old)'), (b'3F', b'Full-day Pre-School (3 Years Old)'), (b'4H', b'Half-day Pre-School (4 Years Old)'), (b'4F', b'Full-day Pre-School (4 Years Old)'), (b'KH', b'Half-day Kindergarten'), (b'KF', b'Full-day Kindergarten'), (b'1', b'Grade 1'), (b'2', b'Grade 2'), (b'3', b'Grade 3'), (b'4', b'Grade 4'), (b'5', b'Grade 5'), (b'6', b'Grade 6'), (b'7', b'Grade 7'), (b'8', b'Grade 8'), (b'9', b'Grade 9'), (b'0', b'Grade 10'), (b'11', b'Grade 11'), (b'12', b'Grade 12'), (b'PG', b'Post Graduate'), (b'AD', b'Adult High School')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
