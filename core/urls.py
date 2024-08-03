
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.static import serve
from info import full_info
from customer_orders.apis.views.customer_station.create import get_previous_quantity_customer_station
schema_view = get_schema_view(
    openapi.Info(
        title="Docs",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('users.urls')),
    path('clients/',include('clients_.urls')),
    path('expenses/',include('expenses.urls')),
    path('employee/',include('employee.urls')),
    path('shift/',include('shift.apis.urls')),
    path('invoices/', include('invoices.apis.urls')),
    path('codes/', include('codes.urls')),
    path('trumpet/', include('trumpet.apis.urls')),
    path('tank/', include('tank.apis.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('settings/',include('settings.apis.urls')),
    path('repository/', include('repository_.apis.urls')),
    path('customers-orders/', include('customer_orders.urls')),
    path('new-purchase/', include('new_purchase.urls')),
    path('cash-station/', include('cash_station.urls')),
    path('reports/', include('reports.urls')),
    path('search/', include('search.apis.urls')),
    path('notifications/', include('notifications.apis.urls')),
    path('previous-quantity/<str:customer_name>/<str:subject_name>/', get_previous_quantity_customer_station),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    ### Info ###
    path('customer-data-without-cars-and-subjects/<str:customer>/', full_info.get_customer_info),
    path('customer-data-with-cars-and-subjects/<str:customer>/', full_info.get_customer_info_with_cars_subjects),
    path('get-trumpet-k/', full_info.get_trumpet_k),
    path('get-branches/', full_info.get_branches)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
