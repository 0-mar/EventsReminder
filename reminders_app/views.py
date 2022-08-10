from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Events


def index(request):
    all_events = Events.objects.all()

    return render(request, 'reminders_app/index.html', {"events": all_events})


def event_detail(request, event):
    evt = get_object_or_404(Events, slug=event)
    return render(request, 'reminders_app/event_detail.html', {"event": evt})


# +-------------------------------------+
# |*************************************|
# |********* DEPRECATED ****************|
# |*************************************|
# +-------------------------------------+
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

