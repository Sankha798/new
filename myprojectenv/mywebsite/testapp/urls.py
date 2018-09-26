from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#url(r'^', views.login, name='index'),
	url(r'^login.html', views.login),
	url(r'^index.html', views.result),
	url(r'^register.html', views.result),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
]
