from django.contrib import admin
from .models import Enrollment, Assignment, Transcript


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course_section', 'semester', 'status', 'grade', 'enrollment_date']
    list_filter = ['semester', 'status', 'grade']
    search_fields = ['student__first_name', 'student__last_name', 'course_section__course__course_code', 'course_section__course__title']
    readonly_fields = ['enrollment_date', 'updated_at']
    
    fieldsets = (
        ('Enrollment Information', {
            'fields': ('student', 'course_section', 'semester', 'status')
        }),
        ('Grades', {
            'fields': ('grade', 'midterm_grade', 'final_grade')
        }),
        ('Timestamps', {
            'fields': ('enrollment_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'enrollment', 'assignment_type', 'due_date', 'points_earned', 'points_possible', 'get_percentage']
    list_filter = ['assignment_type', 'due_date']
    search_fields = ['title', 'enrollment__student__first_name', 'enrollment__student__last_name', 'enrollment__course_section__course__course_code']
    readonly_fields = ['submitted_date', 'graded_date']
    
    fieldsets = (
        ('Assignment Information', {
            'fields': ('enrollment', 'title', 'description', 'assignment_type')
        }),
        ('Grading', {
            'fields': ('points_earned', 'points_possible', 'weight', 'feedback')
        }),
        ('Dates', {
            'fields': ('assigned_date', 'due_date', 'submitted_date', 'graded_date')
        }),
    )


@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    list_display = ['student', 'cumulative_gpa', 'total_credits_earned', 'total_credits_attempted', 'generated_date']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_id']
    readonly_fields = ['cumulative_gpa', 'total_credits_earned', 'total_credits_attempted', 'generated_date']
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Academic Summary', {
            'fields': ('cumulative_gpa', 'total_credits_earned', 'total_credits_attempted')
        }),
        ('Honors', {
            'fields': ('academic_honors',)
        }),
        ('Generated', {
            'fields': ('generated_date',)
        }),
    )