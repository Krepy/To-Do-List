from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Note(models.Model):
    noteText = models.CharField(max_length=200)
    todoDate = models.DateField('todo date')

    def __str__(self):
        return self.noteText
    def isToday(self):
        return timezone.now().date() == self.todoDate <= timezone.now().date()
    def isThisWeek(self):
        return timezone.now().date() <= self.todoDate <= timezone.now().date() + datetime.timedelta(days = 6)
    def isExpired(self):
        return self.todoDate < timezone.now().date()
