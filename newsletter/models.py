from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(unique = True)
	full_name = models.CharField(max_length = 120, blank = False, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	# always migrate after adding classes(tables)
	# C:\Users\LAPTOP\Desktop\PythonProject\quiz\src>python manage.py makemigrations
	# Migrations for 'newsletter':
 #  	0001_initial.py:
 #    - Create model SignUp
 # then python manage.py migrate

	def __unicode__(self): #__str__ for python 3.x
		return self.email