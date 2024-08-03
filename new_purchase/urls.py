from django.urls import path, include
urlpatterns = [
    path('new-supplier/', include('new_purchase.apis.views.new-supplier.urls')),
    path('new-purchase/', include('new_purchase.apis.views.new-purchase.urls')),
]
