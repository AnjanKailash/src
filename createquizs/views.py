 from django.shortcuts import render

# Create your views here.
def addquestions(request):
	return render(request, "addquestions.html", {})