from rest_framework import serializers
from info.models import MainInfo, ContactUs, TeamMember, FAQs, PreviousProject, SubscribedEmails, Company


class MainInfoSerializer(serializers.ModelSerializer):
    whatsapp_link = serializers.CharField(read_only=True)

    class Meta:
        model = MainInfo
        fields = ('facebook', 'instagram', 'twitter', 'telegram', 'email', 'address', 'why_us', 'about_us', 'whatsapp',
                  'whatsapp_link')


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        exclude = ('created', 'updated')


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        exclude = ('created', 'updated')


class FAQsSerializer(serializers.ModelSerializer):
    answer = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = FAQs
        exclude = ('created', 'updated')


class PreviousProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreviousProject
        exclude = ('created', 'updated')


class SubscribedEmailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribedEmails
        exclude = ('created', 'updated')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ('created', 'updated')
