from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import AcademicEvent, Semester, UniversityHoliday
from apps.students.models import Student
from datetime import datetime


class AcademicCalendarView(View):
    """View academic calendar with all events"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = Student.objects.get(student_id=student_id)
        
        # Get current semester
        current_semester = Semester.objects.filter(is_current=True).first()
        
        # Get all active events
        events = AcademicEvent.objects.filter(is_active=True).order_by('start_date')
        
        # Get upcoming events
        today = datetime.now().date()
        upcoming_events = AcademicEvent.objects.filter(
            is_active=True,
            start_date__gte=today
        ).order_by('start_date')[:10]
        
        # Get university holidays
        holidays = UniversityHoliday.objects.filter(date__gte=today).order_by('date')[:5]
        
        context = {
            'student': student,
            'current_semester': current_semester,
            'events': events,
            'upcoming_events': upcoming_events,
            'holidays': holidays,
        }
        return render(request, 'calendar/academic_calendar.html', context)


class SemesterInfoView(View):
    """View semester-specific information"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = Student.objects.get(student_id=student_id)
        
        # Get all semesters
        semesters = Semester.objects.filter(is_active=True).order_by('-start_date')
        
        # Get current semester
        current_semester = Semester.objects.filter(is_current=True).first()
        
        context = {
            'student': student,
            'semesters': semesters,
            'current_semester': current_semester,
        }
        return render(request, 'calendar/semester_info.html', context)