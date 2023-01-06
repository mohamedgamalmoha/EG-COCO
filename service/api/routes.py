from django.urls import path

from .views import ServiceListAPIView, PackageListAPIView


app_name = "service"

urlpatterns = [
    path('service/all/', ServiceListAPIView.as_view(), name='service_all'),
    path('package/all/', PackageListAPIView.as_view(), name='package_all')
]
