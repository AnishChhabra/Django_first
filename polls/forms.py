from django import forms
from django.contrib.auth.models import User

from .models import MyUser, MyUserChange_pw, MyUserEdit

class LoginForm(forms.ModelForm):
	
	Password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = MyUser
		fields = ('Username', 'Password')
		
class SignUpForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')

class Change_pwForm(forms.ModelForm):
	
	Old_pw = forms.CharField(widget=forms.PasswordInput())
	New_pw = forms.CharField(widget=forms.PasswordInput())
	New_pw1 = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = MyUserChange_pw
		fields = ('Old_pw', 'New_pw', 'New_pw1')

class EditForm(forms.ModelForm):
	
	Password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = MyUserEdit
		fields = ('Password', 'Firstname', 'Lastname', 'Email')
