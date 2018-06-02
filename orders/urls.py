from django.conf.urls import url
from .views import OrderRUDView,OrderAPIView

#from django.contrib import admin


urlpatterns = [
    url(r'^$', OrderAPIView.as_view(), name='order-list'),
    url(r'^(?P<id>\d+)/$', OrderRUDView.as_view(),name='order_rud_post')
]