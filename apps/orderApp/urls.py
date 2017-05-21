from django.conf.urls import url

from .views import login, regist, index, logout

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'regist/$', regist, name='regist'),
    url(r'index/$', index, name='index'),
    url(r'logout/$', logout, name='logout')
    ]
