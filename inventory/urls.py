from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^show/(?P<student_id>[0-9]+)/$', views.showStudent, name='showStudent'),
	url(r'^edit/(?P<student_id>[0-9]+)/$', views.editStudent, name='editStudent'),
	url(r'^userSearch/$', views.studentSearch, name='studentSearch'),
	url(r'^programs/$', views.program_index, name='program_index'),
	url(r'^programs/(?P<pk>[0-9]+)$', views.program_show, name='program_show'),

]