#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import Dish, DishesType
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

#进入系统菜单页面
class MenuView(View):
    """
    菜品信息列表功能
    """
    def get(self, request):
        all_dishes = Dish.objects.all()
        dish_nums = all_dishes.count()
        all_dtypes = DishesType.objects.all()

        #对菜单列表进行翻页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_dishes, request=request, per_page=5)
        dishes = p.page(page)
        return render(request, 'orderApp/menu.html', {
            'dish_nums': dish_nums, 'all_dtypes': all_dtypes, 'all_dishes': dishes})