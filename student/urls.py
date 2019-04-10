from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

from . import views

app_name = "student"

urlpatterns = [
	url(r"^home/", views.index, name="student_home"),
	url(r"^account/$", views.account, name="student_account"),
	url(r"semester/", views.semester_marks, name="student_semester"),
	url(r"^notes/", views.notes, name="student_notes"),
	url(r"^logout/$", views.logout_view, name="student_logout")
]

