from inventory.models import *
from django.shortcuts import get_object_or_404, redirect, render_to_response, render
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
import requests, json

def device_search(request, student_id=0):
	query = request.POST.get('search', 0)
	if query == 0:
		if student_id == 0:
			return render(request, 'inventory/device_search.html')
		else:
			student = get_object_or_404(Student, student_id=student_id)
			return render(request, 'inventory/device_search.html', {'student':student})
	else:
		results = Device.objects.all().filter(
			Q(name__icontains=query) |
			Q(serial_number__icontains=query) |
			Q(mac_address__icontains=query))
		if len(results) == 0:
			messages.error(request, "No Devices Found!")
			if student_id == 0:
				HttpResponse('option 1')
				return render(request, 'inventory/device_search.html')
			else:
				student = get_object_or_404(Student, student_id=student_id)
				HttpResponse('option 2')
				return render(request, 'inventory/device_search.html', {'student':student})
		else:
			if student_id == 0:
				HttpResponse('option 3')
				return render(request, 'inventory/device_search.html', {'data': results, 'query': query })
			else:
				student = get_object_or_404(Student, student_id=student_id)
				HttpResponse('option 4')
				return render(request, 'inventory/device_search.html', {'data': results, 'query': query, 'student':student })


def device_assign(request, student_id, pk):
	status_id = request.POST.get('status', 0)
	device = get_object_or_404(Device, pk=pk)
	student = get_object_or_404(Student, student_id=student_id)
	if status_id == 0:
		status = Status.objects.all()
		return render(request, 'inventory/device_assign.html', {'student':student, 'device': device, 'status': status})
	else:
		status = get_object_or_404(Status, pk=status_id)
		device.student = student
		device.status = status
		device.save()

		return redirect('inventory:student_show', student_id=student.student_id)

def device_show(request, pk):
	device = get_object_or_404(Device, pk=pk)
	return render(request, 'inventory/device_show.html', {'device': device})

def device_print(request, pk):
	device = get_object_or_404(Device, pk=pk)
	return render(request, 'inventory/device_print.html', {'device': device})

def device_import_select(request):
	flag = 0
	data = 0
	if settings.JSS_URL == '':
		messages.error(request, "JSS URL not set!")
		flag = 1
	if settings.JSS_USER == '':
		messages.error(request, 'JSS User not set!')
		flag = 1
	if settings.JSS_PASSWORD == '':
		messages.error(request, 'JSS Password not set!')
		flag = 1
	if flag == 1:
		return render(request, 'inventory/device_import.html')
	else:
		url = settings.JSS_URL + "/advancedcomputersearches"
		headers = {'Accept':"application/json"}
		r = requests.get(url, headers = headers, auth=(settings.JSS_USER, settings.JSS_PASSWORD))
		if r.status_code == 200:
			data = r.json()
			data = data['advanced_computer_searches']
		else:
			messages.error(request, 'Error Retrieving Computer List! Status Code: ' + str(r.status_code))
		return render(request, 'inventory/device_import_select.html', {'data': data })


def device_import(request, group_id):
	flag = 0
	data = 0
	existsCount = 0
	importCount = 0
	if settings.JSS_URL == '':
		messages.error(request, "JSS URL not set!")
		flag = 1
	if settings.JSS_USER == '':
		messages.error(request, 'JSS User not set!')
		flag = 1
	if settings.JSS_PASSWORD == '':
		messages.error(request, 'JSS Password not set!')
		flag = 1
	if flag == 1:
		return render(request, 'inventory/device_import.html')
	else:
		url = settings.JSS_URL + "/advancedcomputersearches/id/" + group_id
		headers = {'Accept':"application/json"}
		r = requests.get(url, headers = headers, auth=(settings.JSS_USER, settings.JSS_PASSWORD))
		if r.status_code == 200:
			data = r.json()
			data = data['advanced_computer_search']['computers']
			for device in data:
				if Device.objects.filter(serial_number__iexact = device['Serial_Number']).exists():
					messages.info(request, "Device " + device['Computer_Name'] + " already exists")
					existsCount += 1
				else:
					d = Device(name = device['Computer_Name'], serial_number = device['Serial_Number'], mac_address = device['Wifi_Mac_Address'], model = device['Model'])
					d.save()
					messages.success(request, "Device " + device['Computer_Name'] + " imported sucessfully")
					importCount += 1
		else:
			messages.error(request, 'Error Retrieving Computer List! Status Code: ' + str(r.status_code))
		totalCount = importCount + existsCount
		return render(request, 'inventory/device_import_complete.html', { 'totalCount':totalCount, 'existsCount':existsCount, 'importCount':importCount })



