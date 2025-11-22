from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email','first_name', 'last_name', 'password']

    def create(self, validated_data):

        # Heere i have to override create to ensurw that the password is hashed
        user = User.objects.create_user(
            username=validated_data['email'], # We are using the email as username
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user