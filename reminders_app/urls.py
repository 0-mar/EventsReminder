from django.urls import path

from . import views

app_name = 'reminders_app'

urlpatterns = [
    path('', views.index, name='index'),
    # TODO: if anyone creates event with same title, it will crash - needs to be fixed (possibly add the id of the event in URL?)
    path('event/<slug:event>/', views.event_detail, name='event_detail'),
    path('add-event/', views.add_event, name='add_event'),
    path('delete-event/', views.delete_event, name='delete_event'),
]
