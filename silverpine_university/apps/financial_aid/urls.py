from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.FinancialDashboardView.as_view(), name='financial_dashboard'),
    path('aid-packages/', views.FinancialAidPackageView.as_view(), name='financial_aid_packages'),
    path('scholarships/', views.ScholarshipListView.as_view(), name='scholarships'),
    path('payment-history/', views.PaymentHistoryView.as_view(), name='payment_history'),
]