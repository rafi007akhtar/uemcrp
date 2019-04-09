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


class ProfilePic(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	pic = models.ImageField(blank = True)
