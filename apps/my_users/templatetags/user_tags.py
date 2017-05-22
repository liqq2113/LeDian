# coding:utf-8
# __author__ = 'wangchaowei'
# __date__ = '17/4/21 13:58'

from django import template
# from django.utils.safestring import mark_safe
# from django.template.base import resolve_variable, Node, TemplateSyntaxError


register = template.Library()


@register .simple_tag
def error_msg(error_list):
    if error_list:
        return error_list[0]
    return ''
