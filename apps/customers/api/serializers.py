from rest_framework import serializers, permissions
from django.contrib.auth.models import User, Group
from customers.models import Customer
# from rest_framework.authtoken.models import Token
from blogs.api.serializers import BlogSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    class Meta:
        model = User
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    blog = BlogSerializer(required=False)

    # permission_classes

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = self.fields['user']
        if user_data:
            user = user_serializer.create(validated_data=user_data)
            validated_data['user'] = user
        customer_created = Customer.objects.create(**validated_data)
        return customer_created
