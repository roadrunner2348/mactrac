from django.conf.urls import url
from . import views

urlpatterns = [

# Student URLS
	url(r'^students/$', views.student_index, name='student_index'),
	url(r'^students/(?P<student_id>[0-9]+)/$', views.student_show, name='student_show'),
	url(r'^edit/(?P<student_id>[0-9]+)/$', views.editStudent, name='editStudent'),
	url(r'^students/search/$', views.student_search, name='student_search'),
	url(r'^students/(?P<student_id>\w+)/assign/$', views.device_search, name='device_search'),
	url(r'^students/(?P<student_id>\w+)/assign/(?P<pk>\w+)/$', views.device_assign, name='device_assign'),

#Program URLS
	url(r'^programs/$', views.program_index, name='program_index'),
	url(r'^programs/(?P<pk>[0-9]+)$', views.program_show, name='program_show'),

# Devices URLs
	url(r'^devices/search/$', views.device_search, name='device_search'),
	url(r'^devices/(?P<pk>[0-9]+)/$', views.device_show, name='device_show'),
	url(r'^devices/import/$', views.device_import_select, name='device_import_select'),
	url(r'^devices/import/(?P<group_id>[0-9]+)$', views.device_import, name='device_import'),
	


]