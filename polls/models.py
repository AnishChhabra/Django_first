from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django import forms
from django.contrib.auth.models import User

import datetime
#Fields are defined in django.db.models.fields
#Each field is represented by an instance of a FIeld class
#that tells Django abt the type of data in that field.
class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class MyUser(models.Model):

    user = models.OneToOneField(User)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class MyUserChange_pw(models.Model):

    user = models.OneToOneField(User)
    Old_pw = models.CharField(max_length=30)    
    New_pw = models.CharField(max_length=30)
    New_pw1 = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class MyUserEdit(models.Model):

    user = models.OneToOneField(User)
    Password = models.CharField(max_length=30)
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.user.username

class Voter(models.Model):

    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    
    def __str__(self):
        return self.user.username
# Create your models here.