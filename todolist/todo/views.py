from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

def IndexView(self):
    return HttpResponse("Hello, this is a to-do list.")

def TodayView(self):
    return HttpResponse("Hello this is to-do list of today.")

def WeekView(self):
    return HttpResponse("Hello this is to-do list of this week.")

def AddItemView(self):
    return HttpResponse("Hello this is to add items to the to-do list.")

def ExpiredView(self):
    return HttpResponse("Hello this is expired items view.")
