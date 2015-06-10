from django.forms import ModelForm
from django import forms
from .models import Student, Program, Device

class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'student_id', 'state_id', 'school', 'grade_level', 'gender', 'status', 'program']
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)

class StudentEditForm(ModelForm):
	class Meta:
		model = Student
		fields = ['school', 'grade_level', 'gender', 'status', 'program']
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)

class StudentFilterForm(forms.Form):
	GRADE_CHOICES = (
		('ALL', 'All'),
		('3H', 'Half-day Pre-School (3 Years Old)'),
		('3F', 'Full-day Pre-School (3 Years Old)'),
		('4H', 'Half-day Pre-School (4 Years Old)'),
		('4F', 'Full-day Pre-School (4 Years Old)'),
		('KH', 'Half-day Kindergarten'),
		('KF', 'Full-day Kindergarten'),
		('01', 'Grade 1'),
		('02', 'Grade 2'),
		('03', 'Grade 3'),
		('04', 'Grade 4'),
		('05', 'Grade 5'),
		('06', 'Grade 6'),
		('07', 'Grade 7'),
		('08', 'Grade 8'),
		('09', 'Grade 9'),
		('10', 'Grade 10'),
		('11', 'Grade 11'),
		('12', 'Grade 12'),
		('PG', 'Post Graduate'),
		('AD', 'Adult High School')
	)
	grade_level = forms.ChoiceField(label="Grade", choices=GRADE_CHOICES)
	SCHOOL_CHOICES = (
			('ALL', 'All'),
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
	school = forms.ChoiceField(label="School", choices=SCHOOL_CHOICES)
	program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label="All")

	class DeviceEditForm(ModelForm):
		class Meta:
			model = Device
			fields = ['program']
			program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)
