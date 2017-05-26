# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from my_users.models import UserProfile

class DishesType(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'菜品类别')

    class Meta:
        verbose_name = u'菜品类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'菜名')
    image = models.ImageField(upload_to='dish/%Y/%m', max_length=100, verbose_name=u'图片')
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
    product = models.ForeignKey(Dish, default=1, verbose_name=u"菜品")
    unit_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=u"单价")
    quantity = models.IntegerField(default=0, verbose_name=u"菜品数量")

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product

