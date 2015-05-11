from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
import requests, json
import xml.etree.ElementTree as ET
from django.db.models import Q
from .models import Student
from django.shortcuts import get_object_or_404

def index(request):
	return render(request, 'inventory/index.html')

def message(request):
	messages.error(request, "Exterminate!")
	messages.info(request, "Timey Wimey")
	messages.warning(request, "Why'd you go an do that!?")
	messages.success(request, "Alon Zi!")
	messages.debug(request, "The Doctor")
	return render(request, 'inventory/message.html')

def userSearchForm(request):
	return render(request, 'inventory/userSearchForm.html')

def showStudent(request, student_id):
	user = get_object_or_404(Student, student_id=student_id)
	return render(request, 'inventory/show.html', {'user': user})

def editStudent(request, student_id):
	return HttpResponse('GOTCHA!')

def studentSearch(request):

	query = request.POST.get('search', 0)
	if query == 0:
		return render(request, 'inventory/userSearchForm.html')
	else:
		results = Student.objects.all().filter(
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query))
		if len(results) == 0:
			messages.error(request, "No Users Found!")
			return render(request, 'inventory/userSearchForm.html')
		else:
			return render(request, 'inventory/userSearchForm.html', {'data': results, 'query': query })