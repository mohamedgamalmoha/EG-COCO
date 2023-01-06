from rest_framework import serializers
from info.models import MainInfo, ContactUs, TeamMember


class MainInfoSerializer(serializers.ModelSerializer):
    whatsapp_link = serializers.CharField(read_only=True)

    class Meta:
        model = MainInfo
        fields = ('facebook', 'instagram', 'twitter', 'telegram', 'email', 'whatsapp', 'why_us', 'whatsapp_link')


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        exclude = ('created', 'updated')


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        exclude = ('created', 'updated')
