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
				formP = formP.save(commit = False)
				formP.enrollment_number = int(request.user.username)
				print(f"{formP.enrollment_number}, {type(formP.enrollment_number)}, {request.user.username}, {type(request.user.username)}")
				formP.save()
		
		# Contact Details
		try:
			contact = ContactDetails.objects.get(enrollment_number = int(request.user.username))
			formC = ContactDetailsForm(request.POST, instance = contact)
			if formC.is_valid():
				formC.save()
		except:
			formC = ContactDetailsForm(request.POST)
			if formC.is_valid():
				formC = formC.save(commit = False)
				formC.enrollment_number = int(request.user.username)
				formC.save()
		
		# Academic Details
		try:
			acad = AcademicDetails.object.get(enrollment_number = int(request.user.username))
			formA = AcademicDetailsForm(request.POST, instance = acad)
			print("here")
			if formA.is_valid():
				# acad.delete()
				formA.save()
		except:
			formA = AcademicDetailsForm(request.POST)
			if formA.is_valid():
				formA = formA.save(commit = False)
				formA.enrollment_number = int(request.user.username)
				print(f"{formA.enrollment_number}, {type(formA.enrollment_number)}, {request.user.username}, {type(request.user.username)}")
				formA.save()
		
		# Other Details
		try:
			others = OtherDetails(enrollment_number = int(request.user.username))
			formO = OtherDetailsForm(request.POST, instance = others)
			if formO.is_valid():
				others.delete()
				formO.save()
		except:
			formO = OtherDetailsForm(request.POST)
			if formO.is_valid():
				formO = formO.save(commit = False)
				formO.enrollment_number = int(request.user.username)
				formO.save()
		
		# Profile Pic
		try: 
			picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
			pro_pic = ProfilePicForm(request.POST, request.FILES, instance = picture)
			if pro_pic.is_valid():
				pro_pic.save()
		except:
			pro_pic = ProfilePicForm(request.POST, request.FILES)
			if pro_pic.is_valid():
				pro_pic =  pro_pic.save(commit = False)
				pro_pic.enrollment_number = int(request.user.username)
				pro_pic.save()
		
	else:  # GET actions
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

		# Contact Details
		try:
			contact = ContactDetails.objects.get(enrollment_number = int(request.user.username))
			formC = ContactDetailsForm(instance = contact)
		except:
			formC = ContactDetailsForm()

		# Academic Details
		try:
			acad = AcademicDetails.objects.get(enrollment_number = int(request.user.username))
			formA = AcademicDetailsForm(instance = acad)
		except:
			formA = AcademicDetailsForm()

		# Other Details
		try:
			others = OtherDetails.objects.get(enrollment_number = int(request.user.username))
			print(others)
			formO = OtherDetailsForm(instance = others)
		except:
			formO = OtherDetailsForm()

	dici = {
		"user": curr_user, "formP": formP, "pro_pic": pro_pic, "formC": formC,
		"formA": formA, "formO": formO
	}
	return render(request, "student/index.html", dici)

def account(request):
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)
	except:
		pass
	return render(request, "student/student-account.html", {"personal": personal, "pro_pic": pro_pic})

def notes(request):
	if request.method == "POST":
		formN = NotesForm(request.POST)
		if formN.is_valid():
			formN = formN.save(commit = False)
			formN.enrollment_number = int(request.user.username)
			formN.save()
	
	# other things needed
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)
		formN = NotesForm()
		notes = Notes.objects.all().filter(enrollment_number = int(request.user.username))
	except:
		pass
	dici = {"personal": personal, "pro_pic": pro_pic, "formN": formN, "notes": notes}
	return render(request, "student/student_notes.html", dici)

def semester_marks(request):
	try:
		basic = BasicDetails.objects.get(enrollment_number = int(request.user.username))
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)

		# semester marks
		sems = Semester.objects.all().filter(enrollment_number = int(request.user.username))
		averages = [sem.average for sem in sems]
		for i in range(8-len(averages)):
			averages.append("NA")
		print(averages)
	except:
		pass
	sem = basic.current_semester
	dici = {
		"sem": sem, "personal": personal, "pro_pic": pro_pic, 
		"one": averages[0], "two": averages[1], "three": averages[2],
		"four": averages[3], "five": averages[4], "six": averages[5],
		"seven": averages[6], "eight": averages[7]
	}
	return render(request, "student/student_semester.html", dici)

import pandas as pd
def online_test(request):
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)

		# online test
		user = BasicDetails.objects.all().filter(enrollment_number = int(request.user.username))
		sem = user[0].current_semester
		tests = Test.objects.all().filter(semester = sem, is_open = True)

		# read result spreadsheet
		for test in tests:
			sheet_url = str(test.result_url)
			link_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
			df = pd.read_csv(link_url)

			# if no test has been taken yet, break the loop
			if df.shape[0] == 0:
				break

			# skip if test is not taken by the current user
			enrol = df['Enrollment number'][0]
			if enrol != int(request.user.username):
				continue

			# otherwise, retrive the test scores and save them	
			score = df['Score']
			test.result = score[0]
			test.save()
		
		dici = {"personal": personal, "pro_pic": pro_pic, "tests": tests}
	except Exception as e:
		print("Exception:")
		print(e)
	return render(request, "student/student_online.html", dici)

def attendance(request):
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)
	except:
		pass
	return render(request, "student/student_attendance.html", {"personal": personal, "pro_pic": pro_pic})

def assignment(request):
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)

		# will be needed for assignment
		basic = BasicDetails.objects.get(enrollment_number = int(request.user.username))
		sem = basic.current_semester
		sec = basic.current_section
		assignments = Assignment.objects.all().filter(semester=sem, section=sec)
	except:
		pass
	dici = {"personal": personal, "pro_pic": pro_pic, "assignments": assignments}
	return render(request, "student/student_assignment.html", dici)

def payment(request):
	try:
		personal = PersonalDetails.objects.get(enrollment_number = int(request.user.username))
		picture = ProfilePic.objects.get(enrollment_number = int(request.user.username))
		pro_pic = ProfilePicForm(instance = picture)
	except:
		pass
	return render(request, "student/student_payment.html", {"personal": personal, "pro_pic": pro_pic})


def logout_view(request):
	logout(request)
	return redirect("home")

