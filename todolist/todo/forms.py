from django import forms
from django.utils import timezone

from .models import Note
from .widgets import DateInput

class NoteForm(forms.ModelForm):
    noteTitle = forms.CharField(label = 'Title', max_length = 100, widget=forms.TextInput(attrs={
                                                                                                'placeholder' : 'Enter your note title here...'
                                                                                                }))
    noteText = forms.CharField(label = 'Note', widget=forms.Textarea(attrs={
                                                                                'max_length' : 500,
                                                                                'placeholder' : "Enter your note here...",
                                                                                'cols' : 100,
                                                                                'rows' : 5,
                                                                            }))
    todoDate = forms.DateField(label = 'To-Do at', initial=timezone.now().date(), widget=DateInput)

    class Meta:
        model = Note
        fields = ['noteTitle', 'noteText', 'todoDate',]
