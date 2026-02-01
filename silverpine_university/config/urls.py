"""
URL configuration for Silver Pine State University project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('students/', include('apps.students.urls')),
    path('courses/', include('apps.courses.urls')),
    path('grades/', include('apps.grades.urls')),
    path('financial/', include('apps.financial_aid.urls')),
    path('calendar/', include('apps.calendar.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize admin site
admin.site.site_header = "Silver Pine State University Administration"
admin.site.site_title = "SPSU Admin Portal"
admin.site.index_title = "Welcome to Silver Pine State University Admin"