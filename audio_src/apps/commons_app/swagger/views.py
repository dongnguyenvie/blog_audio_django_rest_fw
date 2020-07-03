from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

SCHEMA_VIEW = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', SCHEMA_VIEW)
]
