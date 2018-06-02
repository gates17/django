# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from rest_framework.reverse import reverse as category_reverse

# Create your models here.


class Category(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_category_url(self, request=None):
        return category_reverse("categories:categories_list",  request=request)