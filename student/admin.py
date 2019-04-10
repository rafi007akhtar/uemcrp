from django.contrib import admin
from .models import *

# Register your models here.

## models for student home
admin.site.register(BasicDetails)
admin.site.register(PersonalDetails)
admin.site.register(ProfilePic)
admin.site.register(ContactDetails)
admin.site.register(AcademicDetails)
admin.site.register(OtherDetails)

## model for student notes
admin.site.register(Notes)

## model for semester marks
admin.site.register(Semester)
