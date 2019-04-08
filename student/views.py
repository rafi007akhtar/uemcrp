from django.shortcuts import render
from . import models

# utility functions
import random

# def gen_enrol():
# 	return int(random.uniform(3312019000000000, 3312019999999999))

def gen_regn():
	return int(random.uniform(304201900000000, 304201999999999))

def roll():
	# a class can have maximum 90 students
	return int(random.uniform(1, 90))

import datetime
def semester():
	now = datetime.datetime.now()
	exp = now.year - 2019 + 1
	if (now.month > 6): return exp * 2
	return exp * 2 + 1

def section():
	ind = int(random.uniform(0,5))  # sections available: A-F
	sec = ['A', 'B', 'C', 'D', 'E', 'F']
	return sec[ind]

# Create your views here.
from student.models import BasicDetails

def index(request):
	# fetch the basic details of the student logged in
	try:
		# if logged in before, this won't throw exception
		curr_user = BasicDetails.objects.get(enrollment_number = int(request.user.username))
	except:
		print(f"creating a new user for {request.user.username} of type {type(request.user.username)}")
		# if logged in for the first time without any details
		curr_user = BasicDetails()
		curr_user.enrollment_number = int(request.user.username)  # since user is identified by enrollment number
		curr_user.registration_number = gen_regn()
		curr_user.roll_number = roll()
		curr_user.admission_year = datetime.datetime.now().year
		curr_user.current_semester = semester()
		curr_user.current_section = section()
		curr_user.save()

	return render(request, "student/index.html", {"user": curr_user})

def account(request):
	return render(request, "student/student-account.html")

