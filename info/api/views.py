from rest_framework import generics, permissions

from info.models import MainInfo, ContactUs, TeamMember
from .serializers import MainInfoSerializer, ContactUsSerializer, TeamMemberSerializer


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
