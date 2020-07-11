from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Note
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        Notes = Note.objects.all()
        NotExpiredNotes = [note.id for note in Notes if note.isExpired() != True]
        return Note.objects.filter(id__in=NotExpiredNotes).order_by('todoDate')

class TodayView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        Notes = Note.objects.all()
        TodaysNotes = [note.id for note in Notes if note.isToday()]
        return Note.objects.filter(id__in=TodaysNotes).order_by('todoDate')

class WeekView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        Notes = Note.objects.all()
        WeeksNotes = [note.id for note in Notes if note.isThisWeek()]
        return Note.objects.filter(id__in=WeeksNotes).order_by('todoDate')


class ExpiredView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        Notes = Note.objects.all()
        ExpiredNotes = [note.id for note in Notes if note.isExpired()]
        return Note.objects.filter(id__in=ExpiredNotes).order_by('todoDate')

def AddItemView(self):
    return HttpResponse("Hello this is to add items to the to-do list.")
