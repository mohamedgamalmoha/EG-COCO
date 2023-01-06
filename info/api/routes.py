from django.urls import path

from .views import MainInfoRetrieveAPIView, ContactUsCreateAPIView, TeamMemberListAPIView


app_name = 'info'

urlpatterns = [
    path('main-info/', MainInfoRetrieveAPIView.as_view(), name='main_info_retrieve'),
    path('contact-us/', ContactUsCreateAPIView.as_view(), name='contact_us_create'),
    path('team-member/all/', TeamMemberListAPIView.as_view(), name='team_members_list'),
]
