from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Student model for Silver Pine State University"""
    
    # Personal Information
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    
    # Academic Information
    major = models.CharField(max_length=100)
    minor = models.CharField(max_length=100, blank=True)
    academic_year = models.CharField(max_length=20, choices=[
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ])
    enrollment_date = models.DateField()
    expected_graduation = models.DateField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_credits = models.IntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    academic_standing = models.CharField(max_length=50, choices=[
        ('Good Standing', 'Good Standing'),
        ('Academic Probation', 'Academic Probation'),
        ('Dean\'s List', 'Dean\'s List'),
        ('President\'s List', 'President\'s List'),
    ], default='Good Standing')
    
    # Profile
    profile_picture = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def calculate_gpa(self):
        """Calculate GPA from enrolled courses"""
        from apps.grades.models import Enrollment
        enrollments = Enrollment.objects.filter(student=self, grade__isnull=False)
        
        if not enrollments.exists():
            return 0.00
        
        grade_points = {
            'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0,
            'F': 0.0
        }
        
        total_points = 0
        total_credits = 0
        
        for enrollment in enrollments:
            if enrollment.grade in grade_points:
                points = grade_points[enrollment.grade] * enrollment.course.credits
                total_points += points
                total_credits += enrollment.course.credits
        
        if total_credits == 0:
            return 0.00
        
        return round(total_points / total_credits, 2)