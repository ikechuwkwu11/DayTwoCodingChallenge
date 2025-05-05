from rest_framework import serializers
from .models import User,AccessToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class AccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = ['user','token','created_at']