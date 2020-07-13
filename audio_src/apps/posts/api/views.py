from rest_framework import generics, pagination, response, views, filters, viewsets
from audio_src.apps.posts.models import Post
from audio_src.apps.metas.models import Meta
from audio_src.apps.posts.api.serializers import PostSerializer
from django.http import JsonResponse
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     queryset = None
    #     pk = self.request.query_params.get('pk', None)
    #     pks = self.request.query_params.get('pks', None)
    #     if pk is not None:
    #         queryset = Post.objects.get(pk=pk)
    #         return response.Response(queryset)
    #     elif pks is not None:
    #         pks = [int(x) for x in pks.split(',')]
    #         queryset = Post.objects.filter(pk__in=pks)
    #     else:
    #         queryset = super(PostListAPIView, self).get_queryset()
    #     return queryset


class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'


class PostTrendingListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ['type', 'id']
    # search_fields = ['id']

    # def get_queryset(self):
    #     meta = Meta.objects.filter()
    #     print(meta)
    #     # post = Post.objects.filter()
    #     # print()
    #     paginate_queryset = self.paginate_queryset(post)
    #     serializer = self.serializer_class(paginate_queryset, many=True)
    #     return self.get_paginated_response(serializer.data)
# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]