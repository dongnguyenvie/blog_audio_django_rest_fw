from rest_framework.generics import mixins, GenericAPIView


class ExtendSoftDeleteMixin(mixins.DestroyModelMixin, GenericAPIView):
    """ As we are deleting soft"""

    def perform_destroy(self, instance):
        instance.isDeleted = true
        instance.save()


class ExtendSoftDeleteView(GenericAPIView, ExtendSoftDeleteMixin):
    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
