from django.urls import path, include
from .views.counter import invoices_count
urlpatterns = [
   path('invoices-count/', invoices_count),
   path('deianna-customer-invoice/', include('invoices.apis.views.deianna_customer_invoice.urls')),
   path('deposit-cash-to-the-station/', include('invoices.apis.views.deposit_cash_to_the_station.urls')),
   path('government-expenses-invoice/', include('invoices.apis.views.government_expenses_invoice.urls')),
   path('new-purchasing-clients-invoice/', include('invoices.apis.views.new_purchasing_clients_invoice.urls')),
   path('official-paper-of-employees-invoice/', include('invoices.apis.views.official_papers_of_employees_invoice.urls')),
   path('station-customer-invoice/', include('invoices.apis.views.station_customer_invoice.urls')),
   path('station-expense-invoice/', include('invoices.apis.views.station_expense_invoice.urls')),
   path('trilla-customers/', include('invoices.apis.views.trilla_customers.urls')),
]