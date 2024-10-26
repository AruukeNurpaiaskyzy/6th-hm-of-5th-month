from rest_framework import serializers
from .models import User, List
class UserSeializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=List
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'image']
        read_only_fields = ['user', 'created_at']

