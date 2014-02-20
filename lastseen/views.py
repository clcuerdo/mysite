from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'lastseen/index.html')

def login(request):
	return HttpResponse("Login Page")

def submission(request):
	return HttpResponse("Submission Page")

def profile(request):
	return HttpResponse("Profile Page")
