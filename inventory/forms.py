from django.forms import ModelForm
from django import forms
from .models import Student, Program

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
		