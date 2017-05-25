#coding:utf-8

from django.conf.urls import url

from .views import AddCartView

urlpatterns = [

    #用于添加购物车
    url(r'add_cart/$', AddCartView.as_view(), name='add_cart'),
    ]
