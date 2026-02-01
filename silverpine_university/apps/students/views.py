from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Student


class StudentLoginView(View):
    """Simple name-based login for students"""
    
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        
        if not first_name or not last_name:
            messages.error(request, 'Please enter both first and last name.')
            return render(request, 'auth/login.html')
        
        try:
            student = Student.objects.get(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
                is_active=True
            )
            # Store student ID in session
            request.session['student_id'] = student.student_id
            request.session['student_name'] = student.get_full_name()
            messages.success(request, f'Welcome back, {student.first_name}!')
            return redirect('student_dashboard')
            
        except Student.DoesNotExist:
            messages.error(request, 'Student not found. Please check your name and try again.')
            return render(request, 'auth/login.html')
        except Student.MultipleObjectsReturned:
            messages.error(request, 'Multiple students found with that name. Please contact the registrar.')
            return render(request, 'auth/login.html')


class StudentDashboardView(View):
    """Main student dashboard after login"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id, is_active=True)
        
        # Update GPA
        student.gpa = student.calculate_gpa()
        student.save()
        
        context = {
            'student': student,
        }
        return render(request, 'students/dashboard.html', context)


class StudentLogoutView(View):
    """Logout student"""
    
    def get(self, request):
        request.session.flush()
        messages.success(request, 'You have been logged out successfully.')
        return redirect('student_login')


class StudentProfileView(View):
    """View student profile"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id, is_active=True)
        
        context = {
            'student': student,
        }
        return render(request, 'students/profile.html', context)