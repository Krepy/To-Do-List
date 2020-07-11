from django.test import TestCase
from django.utils import timezone

import datetime
from .models import Notes

# Create your tests here.
class NotesModelTests(TestCase):
    def testIsTodayWithTomorrowsNote(self):
        time = timezone.now() + datetime.timedelta(days = 2)
        TomorrowsNote = Notes(todoDate = time)
        self.assertIs(DayAfterTomorrowsNote.isToday(), False)

    def testIsTodayWithTodaysNote(self):
        time = timezone.now() + datetime.timedelta(days = 1)
        DayAfterTomorrowsNote = Notes(todoDate = time)
        self.assertIs(DayAfterTomorrowsNote.isToday(), False)
