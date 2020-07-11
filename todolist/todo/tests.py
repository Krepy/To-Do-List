from django.test import TestCase
from django.utils import timezone

import datetime
from .models import Notes

# Create your tests here.
class NotesModelTests(TestCase):
    def testIsTodayWithTomorrowsNote(self):
        time = timezone.now().date() + datetime.timedelta(days = 2)
        TomorrowsNote = Notes(todoDate = time)
        self.assertIs(TomorrowsNote.isToday(), False)

    def testIsTodayWithYesterdaysNote(self):
        time = timezone.now().date() - datetime.timedelta(days = 1)
        YesterdaysNote = Notes(todoDate = time)
        self.assertIs(YesterdaysNote.isToday(), False)

    def testIsTodayWithTodaysNote(self):
        time = timezone.now().date()
        TodaysNote = Notes(todoDate = time)
        self.assertIs(TodaysNote.isToday(), True)

    def testIsThisWeekWithNextWeeksNote(self):
        time = timezone.now().date() + datetime.timedelta(days = 7)
        NextWeeksNote = Notes(todoDate = time)
        self.assertIs(NextWeeksNote.isThisWeek(), False)

    def testIsThisWeekWithLastWeeksNote(self):
        time = timezone.now().date() - datetime.timedelta(days = 7)
        LastWeeksNote = Notes(todoDate = time)
        self.assertIs(LastWeeksNote.isThisWeek(), False)

    def testIsThisWeekWithThisWeeksNote(self):
        time = timezone.now().date()
        ThisWeeksNote = Notes(todoDate = time)
        self.assertIs(ThisWeeksNote.isThisWeek(), True)

    def testIsExpiredWithNotExpiredDate(self):
        time = timezone.now().date()
        NotExpired = Notes(todoDate = time)
        self.assertIs(NotExpired.isExpired(), False)

    def testIsExpiredWithExpiredDate(self):
        time = timezone.now().date() - datetime.timedelta(days = 1)
        Expired = Notes(todoDate = time)
        self.assertIs(Expired.isExpired(), True)
