# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class DishesType(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'菜品类别')

    class Meta:
        verbose_name = u'菜品类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'菜名')
    image = models.ImageField(default='dish/%Y/%m', max_length=100, verbose_name=u'图片')
    price = models.FloatField(verbose_name=u'价格')
    type = models.ForeignKey(DishesType, verbose_name=u'菜品类别')
    description = models.TextField(verbose_name=u'描述')
    recipe = models.TextField(verbose_name=u'烹饪方法')
    sales = models.IntegerField(default=0, verbose_name=u'销售数量')

    class Meta:
        verbose_name = u'菜品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ShoppingCart(models.Model):
    dishes = models.ManyToManyField(Dish, verbose_name=u'菜品')
    total_price = models.FloatField(verbose_name=u'总价')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

