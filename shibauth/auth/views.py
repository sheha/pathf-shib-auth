# log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# required
# no auth no view
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")
