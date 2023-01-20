from django.urls import path

from .views import MainInfoRetrieveAPIView, ContactUsCreateAPIView, TeamMemberListAPIView, FAQsListCreateAPIView,\
    PreviousProjectListAPIView, SubscribedEmailsCreateAPIView, CompanyListAPIView


app_name = 'info'

urlpatterns = [
    path('main-info/', MainInfoRetrieveAPIView.as_view(), name='main_info_retrieve'),
    path('contact-us/', ContactUsCreateAPIView.as_view(), name='contact_us_create'),
    path('team-member/all/', TeamMemberListAPIView.as_view(), name='team_members_list'),
    path('FAQs/', FAQsListCreateAPIView.as_view(), name='faq_list_or_create'),
    path('previous-work/all/', PreviousProjectListAPIView.as_view(), name='previous_project_all'),
    path('subscribed-email/', SubscribedEmailsCreateAPIView.as_view(), name='subscribed_emails_create'),
    path('company/all/', CompanyListAPIView.as_view(), name='company_list'),
]
