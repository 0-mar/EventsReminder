from django.urls import path

from . import views

app_name = 'reminders_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:event_id>/<slug:event_slug>/', views.event_detail, name='event_detail'),
    path('add-event/', views.add_event, name='add_event'),
    path('delete-event/', views.delete_event, name='delete_event'),
    path('event/edit/<int:event_id>/<slug:event_slug>/', views.edit_event, name='edit_event'),
]
