# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, mixins
from django.shortcuts import render
from .models import Order
from .serializer import OrderSerializer
from django.db.models import Q

# Create your views here.

class OrderAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # DetailView CreateView FormView
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = OrderSerializer

    # queryset                = BlogPost.objects.all()

    def get_queryset(self):
        qs = Order.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save()  # user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    # pass
    lookup_field = 'id'
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all();

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}