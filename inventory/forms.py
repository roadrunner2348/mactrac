from django.forms import ModelForm
from django import forms
from .models import Student, Program

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['school', 'grade_level', 'gender', 'status', 'program']
		program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label=None)
		