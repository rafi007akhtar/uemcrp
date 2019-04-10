from django import forms
from . import models

class BasicDetailsForms(forms.ModelForm):
	class Meta:
		model = models.BasicDetails
		fields = [
			"enrollment_number", 
			"registration_number", 
			"roll_number",
			"admission_year",
			"current_semester",
			"current_section"
		]

class PersonalDetailsForms(forms.ModelForm):
	class Meta:
		model = models.PersonalDetails
		fields = [
			"name", "DOB", "gender", 
			"name_mother", "name_father",
			"name_guardian", "blood_group"
		]

class ProfilePicForm(forms.ModelForm):
	class Meta:
		model = models.ProfilePic
		fields = ["pic"]

class ContactDetailsForm(forms.ModelForm):
	class Meta:
		model = models.ContactDetails
		fields = [
			"email_id", "mobile_number", "country",
			"state", "city", "pin_code", "address",
			"permanent_address", "guardian_email",
			"guardian_mobile", "guardian_relation"
		]

class AcademicDetailsForm(forms.ModelForm):
	class Meta:
		model = models.AcademicDetails
		fields = [
			"course_id", "tenth_school_name",
			"tenth_board_percentage", "tenth_year_of_passing",
			"tenth_board_name", "twelfth_school_name",
			"twelfth_board_percentage", "twelfth_year_of_passing",
			"twelfth_board_name"
		]

class OtherDetailsForm(forms.ModelForm):
	class Meta:
		model = models.OtherDetails
		fields = [
			"aadhar_number", "category"
		]
