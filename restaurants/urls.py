from django.conf.urls import url

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

urlpatterns = [
    url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    #url(r'^restaurants/create/$', restaurant_createview),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurnats-create'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
    #url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),  
    #url(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]


4:51.36