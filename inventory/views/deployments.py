from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from inventory.models import Student, Device, Status, Program
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def program_index(request):
	program_list = Program.objects.all()
	unassigned_students = Student.objects.filter(program__isnull=True).count()
	unassigned_devices = Device.objects.filter(program__isnull=True).count()
	return render(request, 'inventory/program_index.html', {'program_list': program_list, 'unassigned_devices': unassigned_devices, 'unassigned_students': unassigned_students})

def program_show(request, pk):
	program = get_object_or_404(Program, pk=pk)
	student_list = program.student_set.all().order_by('grade_level', 'last_name', 'first_name')
	paginator = Paginator(student_list, 20)

	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)

	return render_to_response('inventory/program_show.html', {'program': program, 'students': students})