import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class category(models.Model):
	category_name = models.CharField(max_length=200)
	def __unicode__(self): #__str__ for python 3.x
		return self.category_name

class qstns(models.Model):
	category = models.ForeignKey(category)
	question = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
	right_choice = models.CharField(max_length=200)
	marks = models.IntegerField(default = 1)
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
	    return self.date_added >= timezone.now() - datetime.timedelta(days=1)
	# was_published_recently.admin_order_field = 'date_added'
	# was_published_recently.boolean = True
	# was_published_recently.short_description = 'Published recently?'

class choice(models.Model):
	question = models.ForeignKey(qstns)
	choice_text = models.CharField(max_length=200)
	def __unicode__(self):
		return self.choice_text


