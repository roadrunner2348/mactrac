from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^show/(?P<student_id>[0-9]+)/$', views.showStudent, name='showStudent'),
	url(r'^edit/(?P<student_id>[0-9]+)/$', views.editStudent, name='editStudent'),
	url(r'^assign/(?P<student_id>[0-9]+)/$', views.assignStudent, name='assignStudent'),
	url(r'^message/$', views.message, name='message'),
	url(r'^userSearch/$', views.studentSearch, name='studentSearch'),
]