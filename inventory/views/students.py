from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
import requests, json
import xml.etree.ElementTree as ET
from django.db.models import Q
from inventory.models import *
from django.shortcuts import get_object_or_404, redirect
from inventory.forms import StudentForm
from django.contrib.auth.decorators import login_required


def student_index(request):
	students = Student.objects.all();
	return render(request, 'inventory/student_index.html', {'students': students})

def student_show(request, student_id):
	user = get_object_or_404(Student, student_id=student_id)
	return render(request, 'inventory/student_show.html', {'user': user})

def editStudent(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	if request.method == "POST":
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			return redirect('inventory:student_show', student.student_id)
	form = StudentForm(instance=student)
	return render(request, 'inventory/editStudent.html', {'form':form, 'user': student})

def computerAssignSearch(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	query = request.POST.get('search', 0)
	if query == 0:
		return render(request, 'inventory/computerAssignSearch.html', { 'student': student })
	else:
		query = "*" + query + "*"
		jss_url = "http://jss-client.keansburg.k12.nj.us:8080/JSSResource"
		headers = {'accept': 'application/json'}
		r = requests.get(jss_url + "/computers/match/" + query, auth=('checkin','checkin'), headers=headers)
		data = r.json()
		data = data['computers']
		if len(data) == 0:
			messages.error(request, "No Computers Found!")
			return render(request, 'inventry/compuerAssignSearch.html')
		else:
			return render(request, 'inventory/computerAssignSearch.html', {'data': data, 'query': query, 'student_id': student_id })


def student_search(request):

	query = request.POST.get('search', 0)
	program_id = request.POST.get('program', 0)
	grade_id = request.POST.get('grade', 0)
	programs = Program.objects.all()
	grades = Student._meta.get_field('grade_level').choices
	if query == 0:
		return render(request, 'inventory/student_search.html', {'grades': grades, 'programs': programs})
	else:
		results = Student.objects.all().filter(
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query))
		if program_id != '':
			program = get_object_or_404(Program, pk=program_id)
			results = results.filter(program=program)
		if grade_id != '':
			results = results.filter(grade_level=grade_id)
		if len(results) == 0:
			messages.error(request, "No Users Found!")
			return render(request, 'inventory/student_search.html', {'grades': grades, 'programs': programs, 'program_id': program_id, 'grade_id': grade_id })
		else:
			return render(request, 'inventory/student_search.html', {'data': results, 'query': query, 'grades': grades, 'programs': programs, 'program_id': program_id, 'grade_id': grade_id })
