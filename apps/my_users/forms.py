# coding:utf-8
# __author__ = 'wangchaowei'
# __date__ = '17/4/19 18:54'

from django import forms
from captcha.fields import CaptchaField



class LoginForm(forms.Form):
    # username password必须和html里面字段的名称一致，因为是用request.POST(字典类型)传过来的
    username = forms.CharField(required=True, error_messages={'required': u'用户名不能为空'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required': u'密码不能为空', 'min_length': u'最小长度为5'})


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': u'用户名不能为空'})
    email = forms.EmailField(required=True,  error_messages={'required': u'邮箱不能为空'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required': u'密码不能为空', 'min_length': u'最小长度为5'})
    confirm_password = forms.CharField(required=True, min_length=5, error_messages={'required': u'密码不能为空'})
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    # captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

