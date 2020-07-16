from django.conf.urls import url
from audio_src.apps.categories.api.views import CategoryDetailsView, CategoryListView

CategoryDetails = CategoryDetailsView.as_view()
CategoryList = CategoryListView.as_view()

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', CategoryDetails, name='CategoryDetails'),
    url(r'^$', CategoryList, name='CategoryList'),
]
