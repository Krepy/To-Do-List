from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

# Create your models here.
class Note(models.Model):
    noteTitle = models.CharField('Note Title', max_length=100, default = "Placeholder")
    noteText = models.CharField('Note Text', max_length=500)
    todoDate = models.DateField('To-Do at')

    def __str__(self):
        return self.noteText
    def isToday(self):
        return timezone.now().date() == self.todoDate <= timezone.now().date()
    def isThisWeek(self):
        return timezone.now().date() <= self.todoDate <= timezone.now().date() + datetime.timedelta(days = 6)
    def isExpired(self):
        return self.todoDate < timezone.now().date()

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.id})
