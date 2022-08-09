from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    return HttpResponse("Hello, world. You're at the reminders index.")


def user_login(request):
    form = None

    if request.method == "POST":
        form = LoginForm(request.POST)  # instantiate a new form with the submitted data

        if form.is_valid():     # data is valid
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse("Disabled account")

            else:
                return HttpResponse("Invalid login")

    elif request.method == "GET":
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})

