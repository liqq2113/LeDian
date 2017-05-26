#coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Dish, DishesType, ShoppingCart
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

#进入系统菜单页面
class MenuView(View):
    """
    菜品信息列表功能
    """
    def get(self, request):
        all_dishes = Dish.objects.all()
        all_dtypes = DishesType.objects.all()
        # 加入购物车
        product_id = request.GET.get('cart_add', 0)
        if int(product_id) > 0:
            product = Dish.objects.get(id=product_id)
            exist_records = ShoppingCart.objects.filter(product_id=int(product_id))
            if exist_records:
                for record in exist_records:
                    record.quantity += 1
                    record.save()
            else:
                product_add = ShoppingCart()
                if int(product_id) > 0:
                    product_add.product_id = int(product_id)
                    product_add.unit_price = product.price
                    product_add.quantity = 1
                    product_add.save()
                else:
                    return HttpResponse('{"status": "fail", "msg": "You failed"}', content_type='application/json')
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

#搜索
class SearchView(View):
    def post(self, request):
        #搜索功能
        keyword = request.POST.get("keywords", '')
        if keyword:
            all_dish = Dish.objects.all()
            all_dishes = all_dish.filter(Q(name__contains=keyword) | Q(description__contains=keyword))
            if all_dishes:
                all_dtypes = DishesType.objects.all()
                # 取出筛选类别
                type_id = request.GET.get('type', "")
                if type_id:
                    all_dishes = all_dishes.filter(type_id=int(type_id))
                dish_nums = all_dishes.count()
                # 对菜单列表进行翻页
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1

                p = Paginator(all_dishes, request=request, per_page=5)
                dishes = p.page(page)
                return render(request, 'orderApp/menu.html', {
                    'dish_nums': dish_nums, 'all_dtypes': all_dtypes,
                    'all_dishes': dishes, 'type_id': type_id})
            else:
                all_dtypes = DishesType.objects.all()
                # 取出筛选类别
                type_id = request.GET.get('type', "")
                if type_id:
                    all_dishes = all_dishes.filter(type_id=int(type_id))
                dish_nums = all_dishes.count()
                # 对菜单列表进行翻页
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1

                p = Paginator(all_dishes, request=request, per_page=5)
                dishes = p.page(page)
                return render(request, 'orderApp/no_content.html', {
                    'dish_nums': dish_nums, 'all_dtypes': all_dtypes,
                    'all_dishes': dishes, 'type_id': type_id})
        else:
            all_dishes = Dish.objects.all()
            all_rdishes = all_dishes.filter(type_id=1)
            all_special = all_dishes.filter(type_id=6)
            product_id = request.GET.get('cart_add', 0)
            if int(product_id) > 0:
                product = Dish.objects.get(id=product_id)
                exist_records = ShoppingCart.objects.filter(product_id=int(product_id))
                if exist_records:
                    for record in exist_records:
                        record.quantity += 1
                        record.save()
                else:
                    product_add = ShoppingCart()
                    if int(product_id) > 0:
                        product_add.product_id = int(product_id)
                        product_add.unit_price = product.price
                        product_add.quantity = 1
                        product_add.save()
                    else:
                        return HttpResponse('{"status": "fail", "msg": "You failed"}', content_type='application/json')
            ##显示主页面的购物车
            all_products = ShoppingCart.objects.all()
            # 商品数量
            pro_num = 0
            # 运费
            pro_ship = 0
            # 结算金额
            pro_total = 0
            for pro in all_products:
                pro_num += pro.quantity
                pro_ship += pro.quantity * 2
                pro_total += pro.unit_price * pro.quantity
            pro_total += pro_ship
            return render(request, 'index.html', {
                'page_type': 'home', 'all_rdishes': all_rdishes,
                'all_special': all_special, 'pro_num': pro_num,
                'pro_ship': pro_ship, 'pro_total': pro_total})