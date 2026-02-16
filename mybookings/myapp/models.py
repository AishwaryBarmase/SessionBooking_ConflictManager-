# models.py
from django.db import models

class Session(models.Model):
    user_name = models.CharField(max_length=100)
    session_time = models.DateTimeField(unique=True)
    status = models.CharField(max_length=20, default='confirmed')

    class Meta:
        ordering = ['session_time'] # Requirement 3: Sort by time