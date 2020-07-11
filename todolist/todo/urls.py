from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('today', views.TodayView.as_view(), name='today'),
    path('week', views.WeekView.as_view(), name='week'),
    path('expired', views.ExpiredView.as_view(), name='expired'),
    path('add', views.AddItemView, name='add'),
]
