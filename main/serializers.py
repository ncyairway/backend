# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Address, Order, SingleGood, Commodity

User = get_user_model()

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model: Address
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'telephone', 'identity', 'addresses']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'telephone', 'identity']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            telephone=validated_data['telephone'],
            identity=validated_data['identity']
        )
        return user