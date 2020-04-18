from rest_framework import generics
from categories.models import Category
from categories.api.serializers import CategorySerializers


class CategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
