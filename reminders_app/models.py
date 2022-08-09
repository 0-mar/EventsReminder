from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True)  # optional field!py
    user = models.ForeignKey(User, on_delete=models.CASCADE)
