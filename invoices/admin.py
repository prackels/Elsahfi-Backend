from django.contrib import admin

from .models import *

admin.site.register(DeiannaCustomerInvoice)
admin.site.register(StationCustomerInvoice)
admin.site.register(TrillaCustomers)
admin.site.register(NewPurchasingClientsInvoice)
admin.site.register(StationExpenseInvoice)
admin.site.register(GovernmentExpensesInvoice)
admin.site.register(OfficialPapersOfEmployeesInvoice)
admin.site.register(DepositCashToTheStation)