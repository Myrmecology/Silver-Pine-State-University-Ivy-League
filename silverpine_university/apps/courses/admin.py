from django.contrib import admin
from .models import Department, Professor, Course, CourseSection


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'building', 'phone', 'email']
    search_fields = ['code', 'name']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['professor_id', 'first_name', 'last_name', 'title', 'department', 'email']
    list_filter = ['title', 'department']
    search_fields = ['professor_id', 'first_name', 'last_name', 'email']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('professor_id', 'first_name', 'last_name', 'title', 'email', 'profile_picture')
        }),
        ('Department & Office', {
            'fields': ('department', 'office_location', 'office_hours')
        }),
        ('Biography', {
            'fields': ('bio',)
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'title', 'department', 'credits', 'level']
    list_filter = ['department', 'level', 'credits']
    search_fields = ['course_code', 'title', 'description']
    
    fieldsets = (
        ('Course Information', {
            'fields': ('course_code', 'title', 'department', 'description')
        }),
        ('Academic Details', {
            'fields': ('credits', 'level', 'prerequisites')
        }),
    )


@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ['section_id', 'course', 'professor', 'semester', 'days', 'start_time', 'building', 'enrolled_count', 'max_capacity', 'is_active']
    list_filter = ['semester', 'is_active', 'registration_open', 'course__department']
    search_fields = ['section_id', 'course__course_code', 'course__title', 'professor__last_name']
    readonly_fields = ['enrolled_count', 'waitlist_count']
    
    fieldsets = (
        ('Section Information', {
            'fields': ('section_id', 'course', 'professor', 'semester')
        }),
        ('Schedule', {
            'fields': ('days', 'start_time', 'end_time')
        }),
        ('Location', {
            'fields': ('building', 'room_number')
        }),
        ('Enrollment', {
            'fields': ('max_capacity', 'enrolled_count', 'waitlist_count')
        }),
        ('Status', {
            'fields': ('is_active', 'registration_open')
        }),
    )