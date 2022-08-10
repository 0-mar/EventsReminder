from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Events(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique_for_date='date')
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True)  # optional field!
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('reminders_app:event_detail', args=[self.slug, ])
