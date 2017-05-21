#coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(default='/home/liqingqing/图片/1.jpg')
    price = models.FloatField()
    type = models.CharField(max_length=150)
    description = models.TextField()
    recipe = models.TextField()
    sales = models.IntegerField(default=0)


class Img(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField()
    img = models.ImageField(default='/home/liqingqing/图片/1.jpg')
    dish = models.ForeignKey(Dish)
