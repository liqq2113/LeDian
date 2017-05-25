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
    def post(self, request):
        add_id = request.POST.get('add_id', 0)
        add_type = request.POST.get('add_type', 0)

        #判断用户是否登录
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')

        exist_records = ShoppingCart.objects.filter(user=request, add_id=int(add_id), add_type=add_type)
        if exist_records:
            #如果记录已经存在,则数量加１
            pass
        else:
            user_add = ShoppingCart()
            if int(add_id) > 0 and int(add_type) > 0:
                user_add.add_id = int(add_id)
                user_add.add_type = int(add_type)
                user_add.save()
                return HttpResponse('{"status": "fail", "msg": "已加入购物车"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "加入购物车失败"}', content_type='application/json')
