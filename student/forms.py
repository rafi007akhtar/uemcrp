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