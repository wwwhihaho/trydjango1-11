from django.conf.urls import url

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
)

urlpatterns = [
    url(r'^create/$',  ItemCreateView.as_view(), name='create'),         #list를 맨 아래로
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(), name='list'),
]