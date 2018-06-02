# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as order_reverse
# Create your models here.


class Order(models.Model):
    id          = models.AutoField(primary_key=True)
    #user_id
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_order_url(self, request=None):
        return order_reverse("orders:orders_rud_post", kwargs={'id': self.id}, request=request)