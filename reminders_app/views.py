from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from slugify import slugify

from .models import Events
from .forms import EventForm


@login_required
def index(request):
    all_events = Events.objects.all()

    return render(request, 'reminders_app/index.html', {"events": all_events})


@login_required
def event_detail(request, event):
    evt = get_object_or_404(Events, slug=event, user=request.user)
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
            slug = slugify(new_event.title)
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

