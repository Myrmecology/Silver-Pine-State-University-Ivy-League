from django.urls import path
from . import views

urlpatterns = [
    path('academic/', views.AcademicCalendarView.as_view(), name='academic_calendar'),
    path('semesters/', views.SemesterInfoView.as_view(), name='semester_info'),
]