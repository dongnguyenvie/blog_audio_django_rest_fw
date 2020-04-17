from django.conf.urls import url
from customers.api.views import CustomerListAPIView

urlpatterns = [
    url(r'^$', CustomerListAPIView.as_view(), name='list'),
]
