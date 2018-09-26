# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import userform,passwordform
from .models import *
from django.contrib.auth import get_user_model
#from django.http import HttpResponse, HttpResponseDirect


#def index(request):
#	return HttpResponse("Hello, world. You're at the polls index.")
def login(request):
	#if request.method == 'POST':
        #print("check")
        form = userform()
        form1 = passwordform()
	if form.is_valid():
		user = request.POST['emailaddress']
		password = request.POST['password']
		user = loginInfo.authenticate(request, 'username = email', 'password = password')
        return render(request, 'login.html', {'form': form})

def result(request):
        emailaddress = request.GET.get('Emailaddress')
        password = request.GET.get('Password')
	user = loginInfo()
        user.authenticate('username = email', 'password = password')
        if user:
        	return render(request, 'index.html')
	else:
		form = registerInfo()
		return render(request, 'register.html', {'form':form})

# Create your views here.
