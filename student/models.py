from django.db import models

# Create your models here.

class BasicDetails(models.Model):
	enrollment_number = models.IntegerField(default = 0)
	registration_number = models.IntegerField(default = 0)
	roll_number = models.IntegerField(default = 0)
	admission_year = models.IntegerField(default = 0)
	current_semester = models.IntegerField(default = 0)
	current_section = models.CharField(max_length = 2)

