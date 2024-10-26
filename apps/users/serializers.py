
from rest_framework import serializers
import re
from .models import User

class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']

    def validate_phone_number(self, value):
        if not re.match(r'^\+996\d{9}$', value):
            raise serializers.ValidationError("Phone number must be in format +996XXXXXXXXX")
        return value

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id'] 