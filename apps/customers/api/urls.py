from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from customers.api.views import CustomerListAPIView

urlpatterns = [
    url(r'^$', CustomerListAPIView.as_view(), name='list'),
    url('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
