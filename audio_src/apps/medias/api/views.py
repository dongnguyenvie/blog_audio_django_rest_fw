from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.medias.models import Media
from audio_src.apps.medias.api.serializers import MediaSerializer
from audio_src.apps.utils import constants


class MediaListListView(generics.ListCreateAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    ordering = ('-timestamp')
    # filter_backends = [DjangoFilterBackend,
    #                    filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = '__all__'
    # ordering_fields = ('__all__')

    # @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="blogs")
    def list(self, *args, **kwargs):
        return super(MediaListListView, self).list(self, *args, **kwargs)


class MediaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
