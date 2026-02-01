from django.contrib import admin
from .models import FinancialAccount, FinancialAidPackage, Scholarship, Payment


@admin.register(FinancialAccount)
class FinancialAccountAdmin(admin.ModelAdmin):
    list_display = ['student', 'total_charged', 'total_paid', 'account_balance', 'account_status', 'on_payment_plan']
    list_filter = ['account_status', 'on_payment_plan']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_id']
    readonly_fields = ['total_charged', 'account_balance', 'updated_at']
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Charges', {
            'fields': ('tuition_charged', 'fees_charged', 'total_charged')
        }),
        ('Payments', {
            'fields': ('total_paid', 'account_balance')
        }),
        ('Payment Plan', {
            'fields': ('on_payment_plan', 'payment_plan_amount')
        }),
        ('Status', {
            'fields': ('account_status', 'updated_at')
        }),
    )


@admin.register(FinancialAidPackage)
class FinancialAidPackageAdmin(admin.ModelAdmin):
    list_display = ['student', 'academic_year', 'grants', 'scholarships', 'loans', 'work_study', 'total_aid', 'status']
    list_filter = ['academic_year', 'status']
    search_fields = ['student__first_name', 'student__last_name', 'student__student_id']
    readonly_fields = ['total_aid']
    
    fieldsets = (
        ('Student Information', {
            'fields': ('student', 'academic_year')
        }),
        ('Aid Breakdown', {
            'fields': ('grants', 'scholarships', 'loans', 'work_study', 'total_aid')
        }),
        ('Status', {
            'fields': ('status', 'award_date', 'acceptance_date', 'disbursement_date')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Calculate total aid when saving"""
        obj.calculate_total_aid()
        super().save_model(request, obj, form, change)


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'scholarship_type', 'amount', 'minimum_gpa', 'is_active', 'renewable', 'application_deadline']
    list_filter = ['scholarship_type', 'is_active', 'renewable']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Scholarship Information', {
            'fields': ('name', 'description', 'scholarship_type', 'amount')
        }),
        ('Eligibility', {
            'fields': ('minimum_gpa', 'eligibility_requirements')
        }),
        ('Availability', {
            'fields': ('is_active', 'renewable', 'application_deadline')
        }),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['financial_account', 'amount', 'payment_method', 'reference_number', 'payment_date']
    list_filter = ['payment_method', 'payment_date']
    search_fields = ['financial_account__student__first_name', 'financial_account__student__last_name', 'reference_number']
    readonly_fields = ['payment_date']
    
    fieldsets = (
        ('Payment Information', {
            'fields': ('financial_account', 'amount', 'payment_method', 'reference_number')
        }),
        ('Details', {
            'fields': ('payment_date', 'notes')
        }),
    )