from inventory.models import *
from django.shortcuts import get_object_or_404, redirect, render_to_response, render
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse

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

def device_show(request, pk):
	return HttpResponse(pk)

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

		return redirect('inventory:showStudent', student_id=student.student_id)





