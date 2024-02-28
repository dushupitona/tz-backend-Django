from django.contrib import admin

from product.models import *


@admin.register(AuthorModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(LessonModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ['name', 'product_id']


@admin.register(GroupModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ['name']


@admin.register(StudentModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ['name']