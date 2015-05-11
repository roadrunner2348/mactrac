from django.db import models
from django.contrib import admin
from datetime import datetime

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	STATUS_CHOICES = (
			('ACTIVE', 'Active'),
			('INACTIVE', 'Inactive')
		)
	status = models.CharField(max_length=10, choices = STATUS_CHOICES)
	SCHOOL_CHOICES = (
			('KHS', 'Keansburg High School'),
			('BMS', 'Bolger Middle School'),
			('CES', 'Caruso Elementary School'),
			('PMR', 'Port Monmouth Road Elementary'),
			('OOD', 'Out of District Students'),
			('PREG', 'Pre-Registration Students'),
			('INACT', 'Inactive Students'),
			('EARLY', 'Early Intervention'),
			('STVOC', 'State Facility and Full Time Vocational'),
			('SS', 'Summer School KHS')
		)
	school = models.CharField(max_length=6, choices=SCHOOL_CHOICES)
	GENDER_CHOICES = (
			('F','Female'),
			('M','Male'),
		)
	gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)

	@property
	def full_name(self):
		return self.first_name + " " + self.last_name
	student_id = models.PositiveIntegerField(unique = True)
	state_id = models.PositiveIntegerField()
	GRADE_CHOICES = (
		('3H', 'Half-day Pre-School (3 Years Old)'),
		('3F', 'Full-day Pre-School (3 Years Old)'),
		('4H', 'Half-day Pre-School (4 Years Old)'),
		('4F', 'Full-day Pre-School (4 Years Old)'),
		('KH', 'Half-day Kindergarten'),
		('KF', 'Full-day Kindergarten'),
		('1', 'Grade 1'),
		('2', 'Grade 2'),
		('3', 'Grade 3'),
		('4', 'Grade 4'),
		('5', 'Grade 5'),
		('6', 'Grade 6'),
		('7', 'Grade 7'),
		('8', 'Grade 8'),
		('9', 'Grade 9'),
		('0', 'Grade 10'),
		('11', 'Grade 11'),
		('12', 'Grade 12'),
		('PG', 'Post Graduate'),
		('AD', 'Adult High School')
	)
	grade_level = models.CharField(max_length = 2, choices = GRADE_CHOICES)



