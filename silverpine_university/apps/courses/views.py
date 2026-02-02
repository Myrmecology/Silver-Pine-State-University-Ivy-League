from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Course, CourseSection, Department
from apps.students.models import Student
from apps.grades.models import Enrollment


class CourseCatalogView(View):
    """Browse all available courses"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        # Get filter parameters
        department_filter = request.GET.get('department', '')
        level_filter = request.GET.get('level', '')
        search_query = request.GET.get('search', '')
        
        # Base queryset
        courses = Course.objects.all()
        
        # Apply filters
        if department_filter:
            courses = courses.filter(department__code=department_filter)
        if level_filter:
            courses = courses.filter(level=level_filter)
        if search_query:
            courses = courses.filter(
                Q(course_code__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        departments = Department.objects.all()
        
        context = {
            'courses': courses,
            'departments': departments,
            'selected_department': department_filter,
            'selected_level': level_filter,
            'search_query': search_query,
        }
        return render(request, 'courses/catalog.html', context)


class CourseRegistrationView(View):
    """Register for course sections"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get available sections
        sections = CourseSection.objects.filter(
            is_active=True,
            registration_open=True,
            semester='Spring 2026'  # Current registration period
        ).select_related('course', 'professor', 'course__department')
        
        # Get student's current enrollments
        enrolled_sections = Enrollment.objects.filter(
            student=student,
            semester='Spring 2026',
            status='Enrolled'
        ).values_list('course_section_id', flat=True)
        
        # Get shopping cart (stored in session)
        cart = request.session.get('course_cart', [])
        
        context = {
            'student': student,
            'sections': sections,
            'enrolled_sections': list(enrolled_sections),
            'cart': cart,
        }
        return render(request, 'courses/registration.html', context)
    
    def post(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        action = request.POST.get('action')
        section_id = request.POST.get('section_id')
        
        print(f"DEBUG: Action = {action}")
        print(f"DEBUG: Section ID = {section_id}")
        print(f"DEBUG: Cart = {request.session.get('course_cart', [])}")
        
        if action == 'add_to_cart':
            cart = request.session.get('course_cart', [])
            if section_id not in cart:
                cart.append(section_id)
                request.session['course_cart'] = cart
                messages.success(request, 'Course added to cart.')
        
        elif action == 'remove_from_cart':
            cart = request.session.get('course_cart', [])
            if section_id in cart:
                cart.remove(section_id)
                request.session['course_cart'] = cart
                messages.success(request, 'Course removed from cart.')
        
        elif action == 'enroll':
            print("DEBUG: Entering enroll block")
            cart = request.session.get('course_cart', [])
            print(f"DEBUG: Processing {len(cart)} courses from cart")
            
            for sec_id in cart:
                print(f"DEBUG: Processing section {sec_id}")
                section = get_object_or_404(CourseSection, section_id=sec_id)
                
                # Check if already enrolled
                if Enrollment.objects.filter(student=student, course_section=section).exists():
                    print(f"DEBUG: Already enrolled in {section.course.title}")
                    messages.warning(request, f'Already enrolled in {section.course.title}')
                    continue
                
                # Check capacity
                if section.is_full():
                    print(f"DEBUG: {section.course.title} is full")
                    messages.error(request, f'{section.course.title} is full.')
                    continue
                
                # Create enrollment
                enrollment = Enrollment.objects.create(
                    student=student,
                    course_section=section,
                    semester=section.semester,
                    status='Enrolled'
                )
                print(f"DEBUG: Created enrollment: {enrollment}")
                
                # Update enrolled count
                section.enrolled_count += 1
                section.save()
                print(f"DEBUG: Updated seat count for {section.course.title}")
                
                messages.success(request, f'Successfully enrolled in {section.course.title}')
            
            # Clear cart
            request.session['course_cart'] = []
            print("DEBUG: Cart cleared")
        
        return redirect('course_registration')


class CourseScheduleView(View):
    """View student's current schedule"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get current enrollments
        enrollments = Enrollment.objects.filter(
            student=student,
            semester='Spring 2026',
            status='Enrolled'
        ).select_related('course_section', 'course_section__course', 'course_section__professor')
        
        context = {
            'student': student,
            'enrollments': enrollments,
        }
        return render(request, 'courses/schedule.html', context)