#coding:utf-8

from django.conf.urls import url

from .views import AddCartView, CheckCartView, CleanCartView

urlpatterns = [
    #用于查看购物车
    url(r'view_cart/$', AddCartView.as_view(), name='view_cart'),
    #结账
    url(r'checkout/$', CheckCartView.as_view(), name='checkout'),
    #清空购物车
    url(r'clean/$', CleanCartView.as_view(), name='clean'),
    ]
