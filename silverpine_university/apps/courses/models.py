from django.db import models


class Department(models.Model):
    """Academic departments at Silver Pine State University"""
    
    code = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    building = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class Professor(models.Model):
    """Faculty members at Silver Pine State University"""
    
    professor_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=[
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
        ('Adjunct Professor', 'Adjunct Professor'),
    ])
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='professors')
    email = models.EmailField()
    office_location = models.CharField(max_length=100)
    office_hours = models.TextField()
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='professor_profiles/', blank=True, null=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'
    
    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    """Courses offered at Silver Pine State University"""
    
    course_code = models.CharField(max_length=20, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    credits = models.IntegerField(default=3)
    level = models.CharField(max_length=20, choices=[
        ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'),
    ])
    prerequisites = models.TextField(blank=True, help_text="List prerequisite courses")
    
    class Meta:
        ordering = ['course_code']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return f"{self.course_code} - {self.title}"


class CourseSection(models.Model):
    """Specific sections of courses with schedule and enrollment info"""
    
    section_id = models.CharField(max_length=20, unique=True, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='sections')
    semester = models.CharField(max_length=20, choices=[
        ('Fall 2025', 'Fall 2025'),
        ('Spring 2026', 'Spring 2026'),
        ('Summer 2026', 'Summer 2026'),
        ('Fall 2026', 'Fall 2026'),
    ])
    
    # Schedule Information
    days = models.CharField(max_length=10, help_text="e.g., MWF, TR")
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    # Location
    building = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)
    
    # Enrollment
    max_capacity = models.IntegerField(default=30)
    enrolled_count = models.IntegerField(default=0)
    waitlist_count = models.IntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    registration_open = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['semester', 'course__course_code']
        verbose_name = 'Course Section'
        verbose_name_plural = 'Course Sections'
    
    def __str__(self):
        return f"{self.course.course_code} - {self.section_id} ({self.semester})"
    
    def seats_available(self):
        return self.max_capacity - self.enrolled_count
    
    def is_full(self):
        return self.enrolled_count >= self.max_capacity
    
    def get_schedule_display(self):
        return f"{self.days} {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"