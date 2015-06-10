from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
import requests, json
import xml.etree.ElementTree as ET
from django.db.models import Q
from inventory.models import *
from django.shortcuts import get_object_or_404, redirect
from inventory.forms import *
from django.contrib.auth.decorators import login_required


def student_index(request):
	if request.method == "POST":
		form = StudentFilterForm(request.POST)
		grade = request.POST['grade_level']
		school = request.POST['school']
		program = request.POST['program']
		filtered_students = Student.objects.all()
		if grade != "ALL":
			filtered_students = filtered_students.filter(grade_level=grade)
		if school != "ALL":
			filtered_students = filtered_students.filter(school=school)
		if program != "":
			filtered_students = filtered_students.filter(program__id__exact=program)
		return render(request, 'inventory/student_index.html', {'students': filtered_students, 'form': form })
	else:
		students = Student.objects.all()
		form = StudentFilterForm()
		return render(request, 'inventory/student_index.html', {'students': students, 'form': form })

def student_show(request, student_id):
	user = get_object_or_404(Student, student_id=student_id)
	return render(request, 'inventory/student_show.html', {'user': user})

def student_create(request):
	title = "New Student"
	if request.method == "POST":
		form = StudentCreateForm(request.POST)
		if form.is_valid():
			student = form.save()
			return redirect('inventory:student_show', student.student_id)
		else:
			return render(request, 'inventory/student_edit.html', {'form':form, 'title':title })
	form = StudentCreateForm()
	return render(request, 'inventory/student_edit.html', {'form':form, 'title':title })

def student_edit(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	if request.method == "POST":
		form = StudentEditForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			return redirect('inventory:student_show', student.student_id)
	form = StudentEditForm(instance=student)
	title = "Edit: " + student.full_name
	return render(request, 'inventory/student_edit.html', {'form':form, 'user': student, 'title':title })

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
