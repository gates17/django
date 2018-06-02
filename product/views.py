# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, mixins, permissions
from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from django.db.models import Q

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

class ProductAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'id' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = ProductSerializer
    #permission_classes = (permissions.IsAdminUser)

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()#user=self.request.user)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):
    #pass
    lookup_field='id'
    serializer_class = ProductSerializer
    #permission_classes = (permissions.IsAdminUser)

    def get_queryset(self):
        return Product.objects.all();

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
