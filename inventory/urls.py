from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^message/$', views.message, name='message'),
	url(r'^userSearchForm/$', views.userSearchForm, name='userSearchForm'),
	url(r'^userSearch/$', views.userSearch, name='userSearch'),
]