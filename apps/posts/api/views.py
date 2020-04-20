from rest_framework import generics, pagination, response, views
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostListAPIView(generics.ListCreateAPIView):
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


class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
