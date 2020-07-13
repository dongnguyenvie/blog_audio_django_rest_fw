from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from audio_src.apps.customers.api.views import CustomerListAPIView, CustomerAPIView

urlpatterns = [
    url('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^(?P<pk>[0-9a-f-]+)/$', CustomerAPIView.as_view(), name='list'),
    url(r'^$', CustomerListAPIView.as_view(), name='list'),
]
