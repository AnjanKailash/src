from django.shortcuts import render

from .forms import SignUpForm#, CotactForm

# Create your views here.
def home(request):
	title = "Hi" 
	# if request.user.is_authenticated():
	# 	title = "Welcome %s" %(request.user) 
	# if request.method == "POST":
	# 	print request.POST #prints on console

	form = SignUpForm(request.POST or None) #for this we have to import form #request.POST is for validation
	
	context = {
		"template_title": title,
		"form" : form,
	}

	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		full_name=form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "new full name"
		instance.full_name= full_name
		# if instance.full_name == None:
		# 	instance.full_name = "Justin"
		instance.save()
		# print instance.email
		# print instance.timestamp
		context = {
			"template_title":	"Thank you"
	}
	

	# return render(request, "home.html", {})
	return render(request, "home.html", context)

# def contact(request):
# 	form = CotactForm(request.post or None)
# 	context = {
# 		"form" : form,
		

# 	}

# 	return render (request, "forms.html", context)