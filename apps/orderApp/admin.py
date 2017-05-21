from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sales', 'isHot']
    ordering = ['-sales']
    search_fields = ['name']

    def isHot(self, dish):
        return dish.sales > 100
    isHot.short_description = 'hot'
    isHot.boolean = True


admin.site.register(User, UserAdmin)
admin.site.register(Dish, DishAdmin)
