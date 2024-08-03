from django.urls import path
from .views import get, create, update, delete


urlpatterns = [
    path('get/',get.GetTanks),
    path('create/',create.CreateTank),
    path('update/<int:tankid>/',update.UpdateTank),
    path('specify-update/<int:tankid>/',update.specify_update),
    path('update-returend-and-standard/',update.UpdateTankTwoField),
    path('delete/<int:tankid>/',delete.DeleteTank),
    path('get_tanks_details/', get.get_tanks_details)

]