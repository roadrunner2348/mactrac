from django.forms import ModelForm
from django import forms
from .models import Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['school', 'grade_level', 'gender', 'status']
		widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'grade_level': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }