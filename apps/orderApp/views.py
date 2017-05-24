#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import Dish, DishesType


#进入系统菜单页面
class MenuView(View):
    """
    菜品信息列表功能
    """
    def get(self, request):
        all_dishes = Dish.objects.all()
        all_dtypes = DishesType.objects.all()
        return render(request, 'orderApp/menu.html', {'all_dtypes': all_dtypes, 'all_dishes': all_dishes})