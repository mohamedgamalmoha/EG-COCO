from rest_framework import generics, permissions

from info.models import MainInfo, ContactUs, TeamMember, FAQs, PreviousProject, SubscribedEmails, Company
from .serializers import (MainInfoSerializer, ContactUsSerializer, TeamMemberSerializer, FAQsSerializer,
                          PreviousProjectSerializer, SubscribedEmailsSerializer, CompanySerializer)


class MainInfoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MainInfoSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return MainInfo.objects.first()


class ContactUsCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]


class TeamMemberListAPIView(generics.ListAPIView):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.AllowAny]


class FAQsListCreateAPIView(generics.ListCreateAPIView):
    queryset = FAQs.objects.filter(active=True)
    serializer_class = FAQsSerializer
    permission_classes = [permissions.AllowAny]


class PreviousProjectListAPIView(generics.ListAPIView):
    queryset = PreviousProject.objects.filter(active=True)
    serializer_class = PreviousProjectSerializer
    permission_classes = [permissions.AllowAny]


class SubscribedEmailsCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribedEmailsSerializer
    permission_classes = [permissions.AllowAny]


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.filter(active=True)
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]
