from django.urls import path, include

urlpatterns = [
    path('payment-of-the-deadline/', include('cash_station.apis.views.payment-of-the-deadline.urls')),
    path('shift-cash/', include('cash_station.apis.views.shift-cash.urls')),
]
