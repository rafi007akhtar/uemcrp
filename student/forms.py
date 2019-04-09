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
