from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import FinancialAccount, FinancialAidPackage, Scholarship, Payment
from apps.students.models import Student


class FinancialDashboardView(View):
    """Main financial aid dashboard"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get or create financial account
        financial_account, created = FinancialAccount.objects.get_or_create(student=student)
        financial_account.calculate_balance()
        
        # Get current aid packages
        aid_packages = FinancialAidPackage.objects.filter(student=student).order_by('-academic_year')
        
        # Get recent payments
        recent_payments = Payment.objects.filter(financial_account=financial_account)[:5]
        
        # Get available scholarships
        available_scholarships = Scholarship.objects.filter(
            is_active=True,
            minimum_gpa__lte=student.gpa
        )
        
        context = {
            'student': student,
            'financial_account': financial_account,
            'aid_packages': aid_packages,
            'recent_payments': recent_payments,
            'available_scholarships': available_scholarships,
        }
        return render(request, 'financial/dashboard.html', context)


class FinancialAidPackageView(View):
    """View detailed financial aid packages"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get all aid packages
        aid_packages = FinancialAidPackage.objects.filter(student=student).order_by('-academic_year')
        
        context = {
            'student': student,
            'aid_packages': aid_packages,
        }
        return render(request, 'financial/aid_packages.html', context)


class ScholarshipListView(View):
    """Browse available scholarships"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get scholarships student is eligible for
        eligible_scholarships = Scholarship.objects.filter(
            is_active=True,
            minimum_gpa__lte=student.gpa
        )
        
        # Get all scholarships
        all_scholarships = Scholarship.objects.filter(is_active=True)
        
        context = {
            'student': student,
            'eligible_scholarships': eligible_scholarships,
            'all_scholarships': all_scholarships,
        }
        return render(request, 'financial/scholarships.html', context)


class PaymentHistoryView(View):
    """View payment history"""
    
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            messages.warning(request, 'Please log in to continue.')
            return redirect('student_login')
        
        student = get_object_or_404(Student, student_id=student_id)
        
        # Get financial account
        financial_account = get_object_or_404(FinancialAccount, student=student)
        
        # Get all payments
        payments = Payment.objects.filter(financial_account=financial_account).order_by('-payment_date')
        
        context = {
            'student': student,
            'financial_account': financial_account,
            'payments': payments,
        }
        return render(request, 'financial/payment_history.html', context)