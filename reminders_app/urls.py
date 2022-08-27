from django.urls import path

from . import views

app_name = 'reminders_app'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.UpcomingEventsListView.as_view(), name='index'),
    path('done-events/', views.DoneEventsListView.as_view(), name='done_events'),
    path('event/<int:event_id>/<slug:event_slug>/', views.event_detail, name='event_detail'),

    path('add-event/', views.add_event, name='add_event'),
    path('event/edit/<int:event_id>/<slug:event_slug>/', views.edit_event, name='edit_event'),

    # actions
    path('delete-event/', views.delete_event, name='delete_event'),
    path('complete-event/', views.complete_event, name='complete_event'),
    path('undo-event/', views.UndoEventView.as_view(), name='undo_event'),
]
