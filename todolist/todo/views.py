from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Note
from .forms import NoteForm
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

class NoteDetailView(generic.DetailView):
    template_name = 'todo/detail.html'
    model = Note

    def get_note(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Note, pk=pk_)

def NoteDelete(request, pk_):
    get_object_or_404(Note, pk=pk_).delete()

    return HttpResponseRedirect(reverse('todo:index'))


class AddItemView(generic.edit.CreateView):
    form_class = NoteForm
    template_name = 'todo/addNote.html'

    def get_queryset(self):
        return Note.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class NoteUpdateView(generic.edit.UpdateView):
    form_class = NoteForm
    template_name = 'todo/updateNote.html'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Note, pk=pk_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
