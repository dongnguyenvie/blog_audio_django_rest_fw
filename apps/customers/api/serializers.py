from rest_framework import serializers
from django.contrib.auth.models import User
from customers.models import Customer
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    # token = Token.objects.create(user)
    # print(token)

    class Meta:
        model = Customer
        fields = '__all__'
