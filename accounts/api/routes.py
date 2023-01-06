from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet)

app_name = 'accounts'
urlpatterns = [
    path('', include(router.urls), name='user'),
    path('', include('djoser.urls.jwt'), name='auth'),
]
