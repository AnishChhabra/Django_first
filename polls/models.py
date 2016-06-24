from django.db import models
#Fields are defined in django.db.models.fields
#Each field is represented by an instance of a FIeld class
#that tells Django abt the type of data in that field.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

# Create your models here.
