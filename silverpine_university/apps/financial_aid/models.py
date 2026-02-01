from django.db import models
from apps.students.models import Student


class FinancialAccount(models.Model):
    """Student financial account tracking"""
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='financial_account')
    
    # Tuition and Fees
    tuition_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fees_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Payments
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Balance
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Payment plan
    on_payment_plan = models.BooleanField(default=False)
    payment_plan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Status
    account_status = models.CharField(max_length=50, choices=[
        ('Current', 'Current'),
        ('Past Due', 'Past Due'),
        ('Hold', 'Hold - Cannot Register'),
        ('Paid in Full', 'Paid in Full'),
    ], default='Current')
    
    # Timestamps
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Financial Account'
        verbose_name_plural = 'Financial Accounts'
    
    def __str__(self):
        return f"{self.student.get_full_name()} - Balance: ${self.account_balance}"
    
    def calculate_balance(self):
        """Calculate current account balance"""
        self.total_charged = self.tuition_charged + self.fees_charged
        self.account_balance = self.total_charged - self.total_paid
        self.save()


class FinancialAidPackage(models.Model):
    """Financial aid awarded to students"""
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='financial_aid_packages')
    academic_year = models.CharField(max_length=20)
    
    # Aid amounts
    grants = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Need-based grants")
    scholarships = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Merit-based scholarships")
    loans = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Student loans")
    work_study = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Work-study award")
    
    # Total aid
    total_aid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Status
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending Review'),
        ('Awarded', 'Awarded'),
        ('Accepted', 'Accepted by Student'),
        ('Disbursed', 'Disbursed'),
        ('Declined', 'Declined'),
    ], default='Pending')
    
    # Timestamps
    award_date = models.DateField(null=True, blank=True)
    acceptance_date = models.DateField(null=True, blank=True)
    disbursement_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-academic_year']
        verbose_name = 'Financial Aid Package'
        verbose_name_plural = 'Financial Aid Packages'
    
    def __str__(self):
        return f"{self.student.get_full_name()} - {self.academic_year} (${self.total_aid})"
    
    def calculate_total_aid(self):
        """Calculate total financial aid"""
        self.total_aid = self.grants + self.scholarships + self.loans + self.work_study
        self.save()


class Scholarship(models.Model):
    """Available scholarships at Silver Pine State University"""
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    scholarship_type = models.CharField(max_length=50, choices=[
        ('Academic Merit', 'Academic Merit'),
        ('Athletic', 'Athletic'),
        ('Need-Based', 'Need-Based'),
        ('Departmental', 'Departmental'),
        ('Diversity', 'Diversity'),
        ('Leadership', 'Leadership'),
    ])
    
    # Eligibility
    minimum_gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    eligibility_requirements = models.TextField()
    
    # Availability
    is_active = models.BooleanField(default=True)
    renewable = models.BooleanField(default=False)
    application_deadline = models.DateField()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Scholarship'
        verbose_name_plural = 'Scholarships'
    
    def __str__(self):
        return f"{self.name} - ${self.amount}"


class Payment(models.Model):
    """Payment transactions for student accounts"""
    
    financial_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, related_name='payments')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Check', 'Check'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Financial Aid', 'Financial Aid'),
        ('Payment Plan', 'Payment Plan'),
    ])
    
    reference_number = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    # Notes
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
    
    def __str__(self):
        return f"{self.financial_account.student.get_full_name()} - ${self.amount} on {self.payment_date.strftime('%Y-%m-%d')}"