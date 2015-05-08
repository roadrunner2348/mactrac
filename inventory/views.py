from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
import requests, json
import xml.etree.ElementTree as ET
from django.db.models import Q
from .models import Student

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

def newUserSearch(request):
	
	query = request.POST.get('search', 0)
	if query == 0:
		return render(request, 'inventory/userSearchForm.html')
	else:
		jss_url = "http://jss-client.keansburg.k12.nj.us:8080/JSSResource"
		headers = {'accept': 'application/json'}
		r = requests.get(jss_url + "/ldapservers/id/1/user/" + query, auth=('checkin','checkin'), headers=headers)
		data = r.json()
		data = data['ldap_users']
		if len(data) == 0:
			messages.error(request, "No Users Found!")
			return render(request, 'inventory/userSearchForm.html')
		else:
			return render(request, 'inventory/userSearchForm.html', {'data': data, 'query': query })

def userSearch(request):

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