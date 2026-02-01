from django.contrib import admin
from .models import AcademicEvent, Semester, UniversityHoliday


@admin.register(AcademicEvent)
class AcademicEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'end_date', 'semester', 'is_featured', 'is_active']
    list_filter = ['event_type', 'semester', 'is_featured', 'is_active']
    search_fields = ['title', 'description']
    
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description', 'event_type', 'semester')
        }),
        ('Date & Time', {
            'fields': ('start_date', 'end_date', 'all_day', 'start_time', 'end_time')
        }),
        ('Location', {
            'fields': ('location',)
        }),
        ('Visibility', {
            'fields': ('is_active', 'is_featured')
        }),
    )


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'academic_year', 'start_date', 'end_date', 'is_current', 'is_active']
    list_filter = ['is_current', 'is_active', 'academic_year']
    search_fields = ['name', 'academic_year']
    
    fieldsets = (
        ('Semester Information', {
            'fields': ('name', 'academic_year', 'start_date', 'end_date')
        }),
        ('Registration Dates', {
            'fields': ('registration_start', 'registration_end', 'add_drop_deadline', 'withdrawal_deadline')
        }),
        ('Exam Dates', {
            'fields': ('final_exams_start', 'final_exams_end')
        }),
        ('Status', {
            'fields': ('is_current', 'is_active')
        }),
    )


@admin.register(UniversityHoliday)
class UniversityHolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'end_date', 'university_closed', 'classes_cancelled']
    list_filter = ['university_closed', 'classes_cancelled']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Holiday Information', {
            'fields': ('name', 'description', 'date', 'end_date')
        }),
        ('Closure Details', {
            'fields': ('university_closed', 'classes_cancelled')
        }),
    )