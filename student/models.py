from django.db import models

# Create your models here.

class BasicDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	registration_number = models.IntegerField(default = 0)
	roll_number = models.IntegerField(default = 0)
	admission_year = models.IntegerField(default = 0)
	current_semester = models.IntegerField(default = 0)
	current_section = models.CharField(max_length = 2)

class PersonalDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	name = models.CharField(max_length = 100)
	DOB = models.DateField()
	gender = models.CharField(max_length = 2)
	name_mother = models.CharField(max_length = 100)
	name_father = models.CharField(max_length = 100)
	name_guardian = models.CharField(max_length = 100)
	blood_group = models.CharField(max_length = 2)

class ContactDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	email_id = models.EmailField(max_length = 50)
	mobile_number = models.IntegerField()
	country = models.CharField(default = "India", max_length = 100)
	state = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	pin_code = models.IntegerField()
	address = models.CharField(max_length = 200)
	permanent_address = models.CharField(max_length = 200)
	guardian_email = models.EmailField()
	guardian_mobile = models.IntegerField()
	guardian_relation = models.CharField(max_length = 20)

class AcademicDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	course_id = models.CharField(max_length = 10, default = "CS101")
	tenth_school_name = models.CharField(max_length = 100)
	tenth_board_percentage = models.IntegerField(default = 0)
	tenth_year_of_passing = models.IntegerField()
	tenth_board_name = models.CharField(max_length = 50)
	twelfth_school_name = models.CharField(max_length = 100)
	twelfth_board_percentage = models.IntegerField(default = 0)
	twelfth_year_of_passing = models.IntegerField()
	twelfth_board_name = models.CharField(max_length = 50)

class OtherDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	aadhar_number = models.CharField(max_length = 20)
	category = models.CharField(max_length = 3)


class ProfilePic(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	pic = models.ImageField(blank = True)
