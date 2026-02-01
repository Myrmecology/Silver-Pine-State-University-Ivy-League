from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'major', 'academic_year', 'gpa', 'is_active']
    list_filter = ['academic_year', 'academic_standing', 'is_active', 'major']
    search_fields = ['student_id', 'first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'updated_at', 'gpa']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('student_id', 'first_name', 'last_name', 'email', 'phone', 'profile_picture', 'bio')
        }),
        ('Academic Information', {
            'fields': ('major', 'minor', 'academic_year', 'enrollment_date', 'expected_graduation', 'gpa', 'total_credits', 'academic_standing')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Update GPA when saving student"""
        super().save_model(request, obj, form, change)
        obj.gpa = obj.calculate_gpa()
        obj.save()