# contains views functions

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def index(request):
	if request.method == "POST":
		# print("post it is")
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect("student:student_home")
	else:
		form = AuthenticationForm()
		return render(request, "index.html", {"form": form})
		
def student_home(request):
	return render(request, "student-home.html")

