from django import forms
from .models import loginInfo

class userform(forms.Form):
	class Meta:
		model = loginInfo.emailaddress
		fields = ['Email Address']

class passwordform(forms.Form):
	class Meta:
		model = loginInfo.password
		fields = ['Password']
