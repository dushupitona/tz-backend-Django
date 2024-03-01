from django.contrib import admin
from product.models import *


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(LessonModel)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id']


@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']