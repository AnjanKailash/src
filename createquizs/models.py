import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class category(models.Model):
	category_name = models.CharField(max_length=200)
	def __unicode__(self): #__str__ for python 3.x
		return self.category_name

class createquiz(models.Model):
	category = models.ForeignKey(category)
	question = models.CharField(max_length=200)
	date_added = models.DateTimeField("date published")
	right_choice = models.CharField(max_length=200)
	marks = models.IntegerField(default = 1)
	def __unicode__(self):
		return self.question
def was_published_recently(self):
    return self.date_added >= timezone.now() - datetime.timedelta(days=1)

class choice(models.Model):
	question = models.ForeignKey(createquiz)
	choice_text = models.CharField(max_length=200)
	def __unicode__(self):
		return self.choice_text


