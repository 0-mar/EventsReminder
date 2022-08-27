from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class UncompletedEventsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=False)


class DoneEventsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=True)


class Events(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique_for_date='date')
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)  # optional field (null and blank must be set to true)!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    # managers
    objects = models.Manager()  # default manager
    uncompleted_events = UncompletedEventsManager()
    done_events = DoneEventsManager()

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        """Used for reverse URL resolution. Returns URL of Event detail view (page) with corresponding event, based
        on the given slug (each slug corresponds with an Events record in DB).

        Useful when you need the URL for <a href>, for example.
        """
        return reverse('reminders_app:event_detail', args=[self.id, self.slug, ])

    def __str__(self):
        return self.title + "|" + self.slug + "|" + str(self.date)
