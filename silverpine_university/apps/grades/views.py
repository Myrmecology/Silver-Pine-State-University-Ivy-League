from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Enrollment, Transcript, Assignment
from apps.students.models import Student


class TranscriptView(View):
    """View student transcript and GPA"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get or create transcript
        transcript, created = Transcript.objects.get_or_create(student=student)
        transcript.update_transcript()
        
        # Get all completed enrollments
        enrollments = Enrollment.objects.filter(
            student=student,
            status='Completed',
            grade__isnull=False
        ).select_related('course_section', 'course_section__course', 'course_section__professor')
        
        # Group by semester
        semesters = {}
        for enrollment in enrollments:
            semester = enrollment.semester
            if semester not in semesters:
                semesters[semester] = []
            semesters[semester].append(enrollment)
        
        context = {
            'student': student,
            'transcript': transcript,
            'semesters': semesters,
        }
        return render(request, 'grades/transcript.html', context)


class PastClassesView(View):
    """View past completed classes"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get completed courses
        past_enrollments = Enrollment.objects.filter(
            student=student,
            status='Completed'
        ).select_related('course_section', 'course_section__course', 'course_section__professor').order_by('-semester')
        
        context = {
            'student': student,
            'past_enrollments': past_enrollments,
        }
        return render(request, 'grades/past_classes.html', context)


class CurrentGradesView(View):
    """View current semester grades and assignments"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get current enrollments
        current_enrollments = Enrollment.objects.filter(
            student=student,
            semester='Spring 2026',
            status='Enrolled'
        ).select_related('course_section', 'course_section__course', 'course_section__professor')
        
        # Get assignments for each enrollment
        enrollment_data = []
        for enrollment in current_enrollments:
            assignments = Assignment.objects.filter(enrollment=enrollment)
            enrollment_data.append({
                'enrollment': enrollment,
                'assignments': assignments,
            })
        
        context = {
            'student': student,
            'enrollment_data': enrollment_data,
        }
        return render(request, 'grades/current_grades.html', context)