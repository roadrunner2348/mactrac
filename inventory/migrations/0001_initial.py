# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10, choices=[(b'ACTIVE', b'Active'), (b'INACTIVE', b'Inactive')])),
                ('school', models.CharField(max_length=6, choices=[(b'KHS', b'Keansburg High School'), (b'BMS', b'Bolger Middle School'), (b'CES', b'Caruso Elementary School'), (b'PMR', b'Port Monmouth Road Elementary'), (b'OOD', b'Out of District Students'), (b'PREG', b'Pre-Registration Students'), (b'INACT', b'Inactive Students'), (b'EARLY', b'Early Intervention'), (b'STVOC', b'State Facility and Full Time Vocational'), (b'SS', b'Summer School KHS')])),
                ('gender', models.CharField(max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('student_id', models.PositiveIntegerField()),
                ('state_id', models.PositiveIntegerField()),
                ('grade_level', models.CharField(max_length=2, choices=[(b'3H', b'Half-day Pre-School (3 Years Old)'), (b'3F', b'Full-day Pre-School (3 Years Old)'), (b'4H', b'Half-day Pre-School (4 Years Old)'), (b'4F', b'Full-day Pre-School (4 Years Old)'), (b'KH', b'Half-day Kindergarten'), (b'KF', b'Full-day Kindergarten'), (b'01', b'Grade 1'), (b'02', b'Grade 2'), (b'03', b'Grade 3'), (b'04', b'Grade 4'), (b'05', b'Grade 5'), (b'06', b'Grade 6'), (b'07', b'Grade 7'), (b'08', b'Grade 8'), (b'09', b'Grade 9'), (b'10', b'Grade 10'), (b'11', b'Grade 11'), (b'12', b'Grade 12'), (b'PG', b'Post Graduate'), (b'AD', b'Adult High School')])),
            ],
        ),
    ]
