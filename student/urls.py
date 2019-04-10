from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

from . import views

app_name = "student"

urlpatterns = [
	url(r"^home/", views.index, name="student_home"),
	url(r"^account/$", views.account, name="student_account"),
	url(r"^semester/", views.semester_marks, name="student_semester"),
	url(r"^student_online/", views.online_test, name="student_online"),
	url(r"^attendance", views.attendance, name="student_attendance"),
	url(r"^assignment/", views.assignment, name="student_assignment"),
	url(r"^notes/", views.notes, name="student_notes"),
	url(r"^payment/", views.payment, name="student_payment"),
	url(r"^logout/$", views.logout_view, name="student_logout")
]

