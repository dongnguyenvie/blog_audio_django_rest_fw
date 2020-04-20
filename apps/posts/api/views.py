from rest_framework import generics, pagination
from posts.models import Post
from posts.api.serializers import PostSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostListAPIView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = None
        pk = self.request.query_params.get('pk', None)
        pks = self.request.query_params.get('pks', None)
        if pk is not None:
            queryset = Post.objects.filter(pk=pk)
        elif pks is not None:
            pks = [int(x) for x in pks.split(',')]
            queryset = Post.objects.filter(pk__in=pks)
        else:
            queryset = super(PostListAPIView, self).get_queryset()
        return queryset
