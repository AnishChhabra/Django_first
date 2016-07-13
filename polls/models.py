from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django import forms

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
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='dp', blank=True)
    username = models.CharField(max_length=30)
    password = models.CharField(widget=forms.PasswordInput, max_length=30)

    def __str__(self):
        return self.username

class MyUserLogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(widget=forms.PasswordInput, max_length=30)
    def __str__(self):
        return self.username



# Create your models here.
