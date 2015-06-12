from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Student, Program, Device, Status

class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'student_id', 'state_id', 'school', 'grade_level', 'gender', 'status', 'program']
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)

class StudentEditForm(ModelForm):
	class Meta:
		model = Student
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)
		fields = ['school', 'grade_level', 'gender', 'status', 'program']



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
		fields = ['program', 'student']
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)

class DeviceModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name + " - " + obj.serial_number

class CheckOutForm(forms.Form):
	device = DeviceModelChoiceField(queryset=Device.objects.all(), empty_label=None)
	device_status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label=None)

class CheckInForm(forms.Form):
	status = forms.ModelChoiceField(queryset=Status.objects.filter(checkedout=True))
	unassign = forms.BooleanField(initial=False)

class StatusForm(ModelForm):
	class Meta:
		model = Status
		fields = ['name', 'checkedout']