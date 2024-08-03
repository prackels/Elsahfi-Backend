from .apis.cars.views.get import get_car_report
from .apis.customer.get import get_customer_report
from .apis.shift.get import daily_morning_shift_report, daily_evening_shift_report
from .apis.comprehensive_report.comprehensive_report import get_comprehensive_report
from django.urls import path

urlpatterns = [
    path('cars/<str:car>/', get_car_report),
    path('customer/<str:customer>/', get_customer_report),
    path('daily-shift-report-morning/', daily_morning_shift_report),
    path('daily-shift-report-evening/', daily_evening_shift_report),
    path('comprehensive-report/<str:from_date>/<str:to_date>/', get_comprehensive_report),
]
