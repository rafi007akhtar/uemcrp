from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "student/index.html")

def account(request):
	return render(request, "student/student-account.html")

