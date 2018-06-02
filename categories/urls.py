from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryCreateView, CategoryDeleteView, CategoryDetailView, CategoryListView, CategoryUpdateView

#from django.contrib import admin

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name="categories_list"),
    url(r'^create/$', CategoryCreateView.as_view(), name="categories_create"),
    url(r'^update/(?P<id>\d+)/$', CategoryUpdateView.as_view(), name="categories_update"),
    url(r'^detail/(?P<id>\d+)/$', CategoryDetailView.as_view(), name="categories_detail"),
    url(r'^delete/(?P<id>\d+)/$', CategoryDeleteView.as_view(), name="categories_delete"),
]
