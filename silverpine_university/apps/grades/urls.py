from django.urls import path
from . import views

urlpatterns = [
    path('transcript/', views.TranscriptView.as_view(), name='transcript'),
    path('past-classes/', views.PastClassesView.as_view(), name='past_classes'),
    path('current/', views.CurrentGradesView.as_view(), name='current_grades'),
]