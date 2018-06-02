"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tutorial import urls as tutorial_urls
from product import urls as product_urls
from categories import urls as category_urls
from orders import urls as orders_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teste/', include(tutorial_urls)),
    url(r'^product/', include(product_urls, namespace='product')),
    url(r'^orders/', include(orders_urls, namespace='orders')),
    url(r'^categories/', include(category_urls, namespace='categories')),
    #url(r'^product2/', include(product.urls)),
]
