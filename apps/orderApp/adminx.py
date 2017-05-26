# coding:utf-8
# __author__ = 'wangchaowei'
# __date__ = '17/4/19 18:55'

import xadmin
from .models import Dish, DishesType, ShoppingCart


class DishAdmin(object):
    list_display = ['name', 'image', 'price', 'type', 'description', 'recipe', 'sales']
    search_fields = ['name', 'image', 'price', 'type', 'description', 'recipe', 'sales']
    list_filter = ['name', 'image', 'price', 'type', 'description', 'recipe', 'sales']


class DishesTypeAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class ShoppingCartAdmin(object):
    list_display = ['product', 'unit_price', 'quantity']
    search_fields = ['product', 'quantity']
    list_filter = ['product', 'quantity']


xadmin.site.register(Dish, DishAdmin)
xadmin.site.register(DishesType, DishesTypeAdmin)
xadmin.site.register(ShoppingCart, ShoppingCartAdmin)

