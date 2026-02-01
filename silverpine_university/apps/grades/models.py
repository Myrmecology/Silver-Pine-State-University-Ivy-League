from django.db import models
from apps.students.models import Student
from apps.courses.models import CourseSection


class Enrollment(models.Model):
    """Student enrollment in course sections"""
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name='enrollments')
    semester = models.CharField(max_length=20)
    
    # Enrollment status
    status = models.CharField(max_length=20, choices=[
        ('Enrolled', 'Enrolled'),
        ('Waitlisted', 'Waitlisted'),
        ('Dropped', 'Dropped'),
        ('Completed', 'Completed'),
        ('Withdrawn', 'Withdrawn'),
    ], default='Enrolled')
    
    # Grade information
    grade = models.CharField(max_length=2, blank=True, null=True, choices=[
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F'),
        ('P', 'Pass'),
        ('I', 'Incomplete'),
        ('W', 'Withdrawn'),
    ])
    
    midterm_grade = models.CharField(max_length=2, blank=True, null=True)
    final_grade = models.CharField(max_length=2, blank=True, null=True)
    
    # Timestamps
    enrollment_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['student', 'course_section']
        ordering = ['-semester', 'course_section__course__course_code']
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
    
    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course_section.course.course_code} ({self.semester})"
    
    def get_grade_points(self):
        """Convert letter grade to grade points"""
        grade_points = {
            'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0,
            'F': 0.0
        }
        return grade_points.get(self.grade, 0.0)


class Assignment(models.Model):
    """Assignments and grades for courses"""
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    assignment_type = models.CharField(max_length=50, choices=[
        ('Homework', 'Homework'),
        ('Quiz', 'Quiz'),
        ('Exam', 'Exam'),
        ('Project', 'Project'),
        ('Paper', 'Paper'),
        ('Presentation', 'Presentation'),
        ('Lab', 'Lab'),
        ('Participation', 'Participation'),
    ])
    
    # Grading
    points_earned = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    points_possible = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1.0, help_text="Weight in final grade calculation")
    
    # Dates
    assigned_date = models.DateField()
    due_date = models.DateField()
    submitted_date = models.DateTimeField(null=True, blank=True)
    graded_date = models.DateTimeField(null=True, blank=True)
    
    # Feedback
    feedback = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-due_date']
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
    
    def __str__(self):
        return f"{self.title} - {self.enrollment.course_section.course.course_code}"
    
    def get_percentage(self):
        """Calculate percentage score"""
        if self.points_earned is not None and self.points_possible > 0:
            return round((self.points_earned / self.points_possible) * 100, 2)
        return None


class Transcript(models.Model):
    """Official academic transcript for students"""
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='transcript')
    
    # Academic summary
    cumulative_gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_credits_earned = models.IntegerField(default=0)
    total_credits_attempted = models.IntegerField(default=0)
    
    # Academic standing
    academic_honors = models.TextField(blank=True, help_text="Dean's List, President's List, etc.")
    
    # Timestamps
    generated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Transcript'
        verbose_name_plural = 'Transcripts'
    
    def __str__(self):
        return f"Transcript - {self.student.get_full_name()}"
    
    def update_transcript(self):
        """Recalculate transcript data"""
        self.cumulative_gpa = self.student.calculate_gpa()
        
        completed_enrollments = Enrollment.objects.filter(
            student=self.student,
            status='Completed',
            grade__isnull=False
        )
        
        self.total_credits_earned = sum([
            e.course_section.course.credits 
            for e in completed_enrollments 
            if e.grade not in ['F', 'W', 'I']
        ])
        
        self.total_credits_attempted = sum([
            e.course_section.course.credits 
            for e in completed_enrollments
        ])
        
        self.save()