from django.contrib import admin

from .forms import SignUpForm
# Register your models here.
from .models import SignUp #to import tables to admin page from models.py

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	# class Meta:
	# 	model = SignUp
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin) #it shows table named "Sign ups" on admin page