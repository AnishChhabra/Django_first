from django import forms
from django.contrib.auth.models import User

from .models import MyUser, MyUserLogin, MyUserCheck_pw, MyUserEdit

class SignUpForm(forms.ModelForm):
	
	Password = forms.CharField(widget=forms.PasswordInput())
	Password1 = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = MyUser
		fields = ['Firstname', 'Lastname', 'Username', 'Email', 'Password', 'Password1']
		
class LoginForm(forms.ModelForm):
	
	Password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = MyUserLogin
		fields = ['Username', 'Password']

class Check_pwForm(forms.ModelForm):
	
	Old_pw = forms.CharField(widget=forms.PasswordInput())
	New_pw = forms.CharField(widget=forms.PasswordInput())
	New_pw1 = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = MyUserCheck_pw
		fields = ['Old_pw', 'New_pw', 'New_pw1']

class EditForm(forms.ModelForm):
	
	Password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = MyUserEdit
		fields = ['Password', 'Firstname', 'Lastname', 'Email']
