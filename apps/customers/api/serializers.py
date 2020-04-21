from rest_framework import serializers, permissions
from django.contrib.auth.models import User, Group
from customers.models import Customer
# from rest_framework.authtoken.models import Token
from blogs.api.serializers import BlogSerializer
from metas.api.serializers import MetaSerializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    # date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    groups = serializers.StringRelatedField(many=True, read_only=True)
    user_permissions = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'first_name',
                  'last_name', 'email', 'password', 'groups', 'user_permissions')
        # fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    meta = MetaSerializers()
    user = UserSerializer()
    blog = BlogSerializer(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)

    # permission_classes

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        meta_data = validated_data.pop('meta')
        user_serializer = self.fields['user']
        meta_serializer = self.fields['meta']

        if user_data:
            user = user_serializer.create(validated_data=user_data)
            validated_data['user'] = user
        if meta_data:
            meta = meta_serializer.create(validated_data=meta_data)
            validated_data['meta'] = meta
        customer_created = Customer.objects.create(**validated_data)
        return customer_created
