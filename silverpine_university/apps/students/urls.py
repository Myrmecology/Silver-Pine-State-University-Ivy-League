from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.StudentLoginView.as_view(), name='student_login'),
    path('dashboard/', views.StudentDashboardView.as_view(), name='student_dashboard'),
    path('logout/', views.StudentLogoutView.as_view(), name='student_logout'),
    path('profile/', views.StudentProfileView.as_view(), name='student_profile'),
]