from rest_framework import serializers
from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # meta = serializers.StringRelatedField()
    # print(23333333333333333)
    # dong = 1111
    # def get_dong(instance):
        # return '11111'
    class Meta:
        model = Blog
        # fields = ['title', 'meta', 'dong']
        fields = '__all__'