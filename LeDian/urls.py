# coding: utf-8
"""LeDian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from my_users.views import LoginView, RegisterView, HomeView, ActiveUserView
from orderApp.views import MenuView
from LeDian.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    #主页
    url('^$', HomeView.as_view(), name='index'),
    #登录
    url('^login/$', LoginView.as_view(), name='login'),
    #注册
    url('^register/', RegisterView.as_view(), name='register'),
    #后台管理
    url(r'^xadmin/', xadmin.site.urls),
    #菜单
    url('^menu/$', MenuView.as_view(), name='menu'),
    #购物车
    url('^order/', include('orderApp.urls')),
    url('^cart/', include('orderApp.urls')),

    url(r'^captcha/', include('captcha.urls')),
    # 配置上传文件的处理函数
    url(r'media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),  # 把 .* 匹配到的字符串放到 active_code 中
]
