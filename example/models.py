# -*- coding: utf-8 -*-

from django.db import models
from sortedone2many.fields import SortedOneToManyField


class Item(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    items = SortedOneToManyField(Item, sorted=True, blank=True)

    def __str__(self):
        return self.name


class CategorySelf(models.Model):
    name = models.CharField(max_length=50)
    items = SortedOneToManyField('self', sorted=True, related_name='category', blank=True)

    def __str__(self):
        return self.name
