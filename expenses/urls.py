from django.urls import path
from expenses.apis.views.station_exp import get, create, update, delete
from expenses.apis.views.government_exp import get as get_gov , create as create_gov , update as update_gov , delete as delete_gov
from expenses.apis.views.cars_exp import get as get_cars, create as create_cars, update as update_cars, delete as delete_cars
from expenses.apis.views.analytics import analytics
urlpatterns = [
    path('station/get/',get.get_station_expenses),
    path('station/create/',create.create_expenses),
    path('station/update/<int:stationid>/',update.update_station_exp),
    path('station/delete/<int:stationid>/',delete.delete_station_exp),

    path('government/station/get/',get_gov.get_gov_station_expenses),
    path('government/station/create/',create_gov.create_gov_expenses),
    path('government/station/update/<int:stationid>/',update_gov.update_gov_station_exp),
    path('government/station/delete/<int:stationid>/',delete_gov.delete_gov_station_exp),

    path('cars/get/', get_cars.get_cars_expenses),
    path('cars/create/', create_cars.create_cars_expenses),
    path('cars/update/<int:pk>/', update_cars.update_cars_expenses),
    path('cars/delete/<int:pk>/', delete_cars.delete_cars_expenses),

    path('analytics/', analytics.get_expenses_analytics)
]