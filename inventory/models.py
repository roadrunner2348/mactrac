from django.db import models
from django.contrib import admin
from datetime import datetime


class Status(models.Model):
	name = models.CharField(max_length=30)
	inactive = models.BooleanField()

	def __str__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=50)
	short_name = models.CharField(max_length=4)

	def __str__(self):
		return self.name

class Class_Year(models.Model):
	year_of_graduation = models.PositiveIntegerField()
	@property
	def grade_level(self):
		current_year = datetime.now().year
		current_month = datetime.now().month
		if current_month > 6:
			current_year += 1
		grade = 12 - (self.year_of_graduation - current_year)
		if grade == 0:
			return "K"
		elif grade < 0:
			return "PREK"
		else:
			return grade

	def __str__(self):
		return str(self.grade_level)

class Role(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	status = models.ForeignKey(Status)
	school = models.ForeignKey(School)
	GENDER_CHOICES = (
			('F','Female'),
			('M','Male'),
		)
	gender = models.CharField(max_length = 2, choices = GENDER_CHOICES, default='F')

	@property
	def full_name(self):
		return self.first_name + " " + self.last_name


class Student(Person):
	student_id = models.PositiveIntegerField()
	class_year = models.ForeignKey(Class_Year)


class Staff(Person):
	role = models.ForeignKey(Role)
class StaffAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name', 'full_name', 'role', 'status']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'class_year','school']
	list_filter = ['school', 'class_year']

class YearAdmin(admin.ModelAdmin):
	list_display = ['year_of_graduation', 'grade_level']

admin.site.register(Status)
admin.site.register(School)
admin.site.register(Class_Year, YearAdmin)
admin.site.register(Role)
admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)


