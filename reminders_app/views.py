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



