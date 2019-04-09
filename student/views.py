from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import logout

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
from student.models import *
from student.forms import *

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
	
	if request.method == "POST":
		# Personal Details
		try:
			# if already saved
			personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
			formP = PersonalDetailsForms(request.POST, instance = personal)
			if formP.is_valid():
				formP.save()
		except:
			# saving first time
			formP = PersonalDetailsForms(request.POST)
			if formP.is_valid():
				formP.save(commit = False)
				formP.enrollment_number = int(request.user.username)
				formP.save()
		
		# Profile Pic
		try: 
			picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
			pro_pic = ProfilePicForm(request.POST, request.FILES, instance = picture)
			if pro_pic.is_valid():
				pro_pic.save()
		except:
			pro_pic = ProfilePicForm(request.POST, request.FILES)
			if pro_pic.is_valid():
				pro_pic.save(commit = False)
				pro_pic.enrollment_number = int(request.user.username)
				pro_pic.save()
		
	else:
		# Personal Details
		try:	
			personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
			formP = PersonalDetailsForms(instance = personal)
		except:
			formP = PersonalDetailsForms()

		# Profile Pic
		try:
			picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
			pro_pic = ProfilePicForm(instance = picture)
		except:
			pro_pic = ProfilePicForm()


	return render(request, "student/index.html", {"user": curr_user, "formP": formP, "pro_pic": pro_pic})

def account(request):
	return render(request, "student/student-account.html")

def logout_view(request):
	logout(request)
	return redirect("home")

