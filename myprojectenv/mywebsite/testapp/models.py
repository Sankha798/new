# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model

class loginInfo(models.Model):
	emailaddress = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def authenticate(self, username=None, password=None, **kwargs):
		UserModel = get_user_model()
		if username is None:
      	   	    username = kwargs.get(UserModel.USERNAME_FIELD)
		try:
           	    if '@' in username:
	       	        UserModel.USERNAME_FIELD = 'email'
	   	    else:
	       	        UserModel.USERNAME_FIELD = 'username'
 	    	
	   	    user = UserModel._default_manager.get_by_natural_key(username)
		except UserModel.DoesNotExist:
            	    UserModel().set_password(password)
       		else:
   	   	    if user.check_password(password) and self.user_can_authenticate(user):
		        return user
	
class registerInfo(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	emailaddress = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	confirmpassword = models.CharField(max_length=20)
# Create your models here.
