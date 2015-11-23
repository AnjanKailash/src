from django import forms #default for importing all the forms

from .models import SignUp

# class ContactForm(forms.Form):#class = table
# 	full_name = CharField()
# 	email = forms.EmailField()
# 	message = forms.CharField() 


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name","email"]
		# Exclude = ["full_name"]

	def clean_email(self): # to apply validation rules
		# print self.cleaned_data.get("email")
		email = self.cleaned_data.get("email")
		# email_base, provider = email.split("@")
		# domain,extension = provider.split(".")
		# if not domain == "USE":
		# 	raise forms.ValidationError("Please make sure you use your USE email")
		# if not extension == "edu":
		# 	raise forms.ValidationError("Use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		return full_name