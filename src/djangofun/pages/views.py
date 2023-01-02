from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello world</h1>") # string of HTML code
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})
	# return HttpResponse("<h2>Welcome to the Jungle</h2>")

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})
	# return HttpResponse("<h2>Welcome to the Jungle</h2>")