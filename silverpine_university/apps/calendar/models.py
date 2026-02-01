from django.db import models


class AcademicEvent(models.Model):
    """Important academic dates and events"""
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    event_type = models.CharField(max_length=50, choices=[
        ('Registration', 'Registration Period'),
        ('Classes', 'Classes Begin/End'),
        ('Exam', 'Examination Period'),
        ('Break', 'Academic Break'),
        ('Holiday', 'University Holiday'),
        ('Deadline', 'Important Deadline'),
        ('Commencement', 'Commencement Ceremony'),
        ('Orientation', 'Orientation'),
        ('Other', 'Other Event'),
    ])
    
    # Date information
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    all_day = models.BooleanField(default=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    # Academic term
    semester = models.CharField(max_length=20, choices=[
        ('Fall 2025', 'Fall 2025'),
        ('Spring 2026', 'Spring 2026'),
        ('Summer 2026', 'Summer 2026'),
        ('Fall 2026', 'Fall 2026'),
    ])
    
    # Location
    location = models.CharField(max_length=200, blank=True)
    
    # Visibility
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_date', 'start_time']
        verbose_name = 'Academic Event'
        verbose_name_plural = 'Academic Events'
    
    def __str__(self):
        return f"{self.title} - {self.start_date}"
    
    def is_multiday(self):
        """Check if event spans multiple days"""
        return self.end_date and self.end_date != self.start_date


class Semester(models.Model):
    """Semester/Term information"""
    
    name = models.CharField(max_length=20, unique=True)
    academic_year = models.CharField(max_length=10)
    
    # Important dates
    start_date = models.DateField()
    end_date = models.DateField()
    
    registration_start = models.DateField()
    registration_end = models.DateField()
    
    add_drop_deadline = models.DateField()
    withdrawal_deadline = models.DateField()
    
    final_exams_start = models.DateField()
    final_exams_end = models.DateField()
    
    # Status
    is_current = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'
    
    def __str__(self):
        return f"{self.name} ({self.academic_year})"


class UniversityHoliday(models.Model):
    """University holidays and closures"""
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="For multi-day holidays")
    
    # Closure information
    university_closed = models.BooleanField(default=True)
    classes_cancelled = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'University Holiday'
        verbose_name_plural = 'University Holidays'
    
    def __str__(self):
        return f"{self.name} - {self.date}"