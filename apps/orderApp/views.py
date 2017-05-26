#coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Dish, DishesType, ShoppingCart
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

#进入系统菜单页面
class MenuView(View):
    """
    菜品信息列表功能
    """
    def get(self, request):
        all_dishes = Dish.objects.all()
        all_dtypes = DishesType.objects.all()
        #取出筛选类别
        type_id = request.GET.get('type', "")
        if type_id:
            all_dishes = all_dishes.filter(type_id=int(type_id))
        dish_nums = all_dishes.count()
        #对菜单列表进行翻页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_dishes, request=request, per_page=5)
        dishes = p.page(page)
        return render(request, 'orderApp/menu.html', {
            'dish_nums': dish_nums, 'all_dtypes': all_dtypes,
            'all_dishes': dishes, 'type_id': type_id})


class AddCartView(View):
    """
    加入购物车功能
    """
    def get(self, request):
        ##显示主页面的购物车
        items = ShoppingCart.objects.all()
        # 商品数量
        pro_num = 0
        # 运费
        pro_ship = 0
        # 结算金额
        pro_total = 0
        for pro in items:
            pro_num += pro.quantity
            pro_ship += pro.quantity * 2
            pro_total += pro.unit_price * pro.quantity
        pro_total += pro_ship
        return render(request, 'orderApp/cart.html', {
            'items': items, 'pro_num': pro_num, 'pro_ship': pro_ship,
            'pro_total': pro_total})


#结账
class CheckCartView(View):
    def get(self, request):
        return render(request, 'orderApp/check.html')

#清空购物车
class CleanCartView(View):
    def get(self, request):
        all_products = ShoppingCart.objects.all()
        all_products.delete()
        ##已清空

        all_dishes = Dish.objects.all()
        all_rdishes = all_dishes.filter(type_id=1)
        all_special = all_dishes.filter(type_id=6)

        #显示购物车页面
        items = ShoppingCart.objects.all()
        # 商品数量
        pro_num = 0
        # 运费
        pro_ship = 0
        # 结算金额
        pro_total = 0
        for pro in items:
            pro_num += pro.quantity
            pro_ship += pro.quantity * 2
            pro_total += pro.unit_price * pro.quantity
        pro_total += pro_ship
        return render(request, 'orderApp/cart.html', {
            'pro_num': pro_num, 'items': items,
            'pro_ship': pro_ship, 'pro_total': pro_total})



