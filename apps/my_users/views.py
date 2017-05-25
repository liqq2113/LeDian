# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import LoginForm, RegisterForm
from .models import UserProfile, EmailVerifyRecord
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from utils.email_send import send_register_email
from orderApp.models import Dish, DishesType

class ActiveUserView(View):

    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'my_users/register_succ.html')
        else:
            return render(request, 'my_users/active_fail.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'my_users/index.html', {'login_btn_msg': 'ready'})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is None:
                return render(request, 'my_users/index.html', {'msg': u'用户名或密码错误！', 'login_btn_msg': 'ready'})
            else:
                if user.is_active:
                    login(request, user)
                    return render(request, 'my_users/login_succ.html', {'login_btn_msg': 'click'})
                else:
                    return render(request, 'my_users/index.html', {'msg': u'用户未激活！', 'login_btn_msg': 'ready'})
        else:
            return render(request, 'my_users/index.html', {'login_form': login_form, 'login_btn_msg': 'ready'})


class RegisterView(View):
    def get(self, request):
        a = request.GET.get('page_type', '')
        if request.GET.get('newsn') == '1':
            csn = CaptchaStore.generate_key()
            cimageurl = captcha_image_url(csn)
            return HttpResponse(cimageurl)

        register_form = RegisterForm()
        return render(request, 'my_users/register.html', {
            'register_form': register_form,
            'register_btn_msg': 'ready',
            'page_type': request.GET.get('page_type', ''),
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'my_users/register.html', {
                    'register_form': register_form,
                    'msg': u'用户已经存在',
                    'page_type': request.POST.get('page_type', ''),
                    'register_btn_msg': 'ready',
                })
            if UserProfile.objects.filter(email=email):
                return render(request, 'my_users/register.html', {
                    'register_form': register_form,
                    'msg': u'邮箱已经存在',
                    'page_type': request.POST.get('page_type', ''),
                    'register_btn_msg': 'ready',
                })

            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()  # 保存到数据库中

            send_register_email(email, 'register')
            return render(request, 'my_users/wait_active.html')
        else:
            return render(request, 'my_users/register.html', {
                'register_form': register_form,
                'register_btn_msg': 'ready',
                'page_type': request.POST.get('page_type', ''),
            })


class HomeView(View):
    def get(self, request):
        all_dishes = Dish.objects.all()
        all_rdishes = all_dishes.filter(type_id=1)
        all_special = all_dishes.filter(type_id=6)
        return render(request, 'index.html', {'page_type': 'home', 'all_rdishes': all_rdishes, 'all_special': all_special})

