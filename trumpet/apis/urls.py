from django.urls import path
from .views.analytics import get_reading_trumpet_analytics
from .views.trumpet import get as get_trumpet, create as create_trumpet, delete as delete_trumpet, update as update_trumpet
from .views.reading_trumpet import create as create_reading, get as get_reading, delete as delete_reading, update as update_reading
urlpatterns = [
    path('get/', get_trumpet.get_trumpets),
    path('get-by/<str:material_name>/', get_trumpet.get_trumpets_by_material),
    path('create/', create_trumpet.create_trumpet),
    path('delete/<int:pk>/', delete_trumpet.delete_trumpet),
    path('update/<int:pk>', update_trumpet.update_trumpet),

    path('reading-trumpet/get/', get_reading.get_reading_trumpet),
    path('reading-trumpet/create/', create_reading.create_reading_trumpet),
    path('reading-trumpet/delete/<int:pk>/', delete_reading.delete_reading_trumpet),
    path('reading-trumpet/update/<int:pk>/', update_reading.update_reading_trumpet),

    path('reading-trumpet-k/get/', get_reading.get_reading_trumpet_k),
    path('reading-trumpet-k/create/', create_reading.create_reading_trumpet_k),
    path('reading-trumpet-k/delete/<int:pk>/', delete_reading.delete_reading_trumpet_k),
    path('reading-trumpet-k/update/<int:pk>/', update_reading.update_reading_trumpet_k),

    path('analytics/<str:from_date>/<str:to_date>/', get_reading_trumpet_analytics.get_reading_trumpet_with_date),
]