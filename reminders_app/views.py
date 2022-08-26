from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from slugify import slugify
import datetime

from .models import Events
from .forms import EventForm


@login_required
def index(request):
    today = datetime.date.today()
    all_events = Events.objects.all().filter(user=request.user)

    return render(request, 'reminders_app/index.html', {"events": all_events, "today_date": today})


@login_required
def event_detail(request, event_id, event_slug):
    evt = get_object_or_404(Events, pk=event_id, slug=event_slug, user=request.user)
    return render(request, 'reminders_app/event_detail.html', {"event": evt})


@login_required
def add_event(request):
    new_event = None

    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            # create Events object but dont add it to DB yet (we need to generate slug + bind the record with the user)
            new_event = event_form.save(commit=False)
            new_event.user = request.user

            # generate a slug from the title
            slug = slugify(new_event.title, max_length=255)
            if len(slug) > 255:
                slug = slug[:255]
            new_event.slug = slug
            new_event.save()

            messages.success(request, 'Event added successfully.')
            return redirect("reminders_app:index")
    else:
        event_form = EventForm()
        return render(request, 'reminders_app/add_event.html', {"event_form": event_form})


@login_required
def delete_event(request):
    if request.method == "POST":
        event_id = request.POST["event_id"]
        event = Events.objects.get(pk=event_id, user=request.user)
        event.delete()

        return redirect("reminders_app:index")


@login_required
def edit_event(request, event_id, event_slug):
    evt = get_object_or_404(Events, pk=event_id, slug=event_slug, user=request.user)

    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            # update the existing Events object
            evt.title = event_form.cleaned_data["title"]
            evt.description = event_form.cleaned_data["description"]
            evt.date = event_form.cleaned_data["date"]
            if event_form.cleaned_data["time"]:
                evt.time = event_form.cleaned_data["time"]

            # update the slug if title was changed
            slug = slugify(evt.title, max_length=255)
            if len(slug) > 255:
                slug = slug[:255]
            evt.slug = slug
            # save the changes into DB
            evt.save()

            messages.success(request, 'Event edited successfully.')
            return redirect(evt, args=(evt.id, evt.slug))

    else:
        event_form = EventForm(instance=evt)
        return render(request, 'reminders_app/edit_event.html', {"event_form": event_form})
