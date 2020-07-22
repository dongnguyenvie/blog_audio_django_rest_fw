from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from audio_src.apps.users.api.views import UserListView, UserDetailsView, AuthViewSet

urlpatterns = [
    url('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^(?P<pk>[0-9a-f-]+)/$', UserDetailsView.as_view(), name='UserDetailsView'),
    url(r'^$', UserListView.as_view(), name='UserListView'),
    # url('dong/', AuthViewSet, name='AuthViewSet'),
]
