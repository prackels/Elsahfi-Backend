from django.contrib import admin
from .models import GovernmentExpense, StationExpense, CarsExpenses

admin.site.register([GovernmentExpense, StationExpense, CarsExpenses])