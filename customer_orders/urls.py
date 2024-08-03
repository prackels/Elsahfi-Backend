from django.urls import path, include
from .apis.views.analytics.get import get_clients_analytics
urlpatterns = [
    path('customer-station/', include('customer_orders.apis.views.customer_station.urls')),
    path('deiann-customer/', include('customer_orders.apis.views.deianna_customer.urls')),
    path('trilla-customer/', include('customer_orders.apis.views.trilla_customer.urls')),
    path('analytics/', get_clients_analytics)
]