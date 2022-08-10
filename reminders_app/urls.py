from django.urls import path

from . import views

app_name = 'reminders_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<slug:event>/', views.event_detail, name='event_detail')
]