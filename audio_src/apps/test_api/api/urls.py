from django.conf.urls import url
from audio_src.apps.test_api.api import views

urlpatterns = [
    url('home', views.home),
    url('test', views.TestView.as_view({
        'post': 'dong',
        'get': 'importSeedData'
    })),
]
