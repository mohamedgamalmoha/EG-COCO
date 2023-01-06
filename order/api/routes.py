from django.urls import path

from .views import PackageOrderCreateAPIView, CustomOrderCreateAPIView


app_name = 'order'

urlpatterns = [
    path('custom-order/create/', CustomOrderCreateAPIView.as_view(), name='custom_order_create'),
    path('package-order/create/', PackageOrderCreateAPIView.as_view(), name='package_order_create'),
]
