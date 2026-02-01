from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.CourseCatalogView.as_view(), name='course_catalog'),
    path('registration/', views.CourseRegistrationView.as_view(), name='course_registration'),
    path('schedule/', views.CourseScheduleView.as_view(), name='course_schedule'),
]