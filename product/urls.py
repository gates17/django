from django.conf.urls import url
from .views import ProductRUDView,ProductAPIView


urlpatterns = [
    url(r'^$', ProductAPIView.as_view(), name='product-list'),
    url(r'^(?P<id>\d+)/$', ProductRUDView.as_view(), name='product_rud_post')
]