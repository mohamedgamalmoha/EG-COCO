from djoser.serializers import UserCreateSerializer


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'phone_number', 'password')
