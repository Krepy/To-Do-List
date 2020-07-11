from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('today/', views.TodayView.as_view(), name='today'),
    path('week/', views.WeekView.as_view(), name='week'),
    path('expired/', views.ExpiredView.as_view(), name='expired'),
    path('add/', views.AddItemView.as_view(), name='add'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('note/<int:pk_>/delete/', views.NoteDelete, name='delete'),
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
]
