from django import forms
from django.contrib.auth.models import User

from .models import MyUser, MyUserLogin

class SignUpForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['firstname', 'lastname', 'username', 'email', 'password', 'image']
		
class LoginForm(forms.ModelForm):
	class Meta:
		model = MyUserLogin
		fields = ['username', 'password']


