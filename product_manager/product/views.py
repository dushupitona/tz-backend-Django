from django.shortcuts import render
from django.views.generic.list import ListView

from product.models import *

from rest_framework.generics import ListAPIView
from rest_framework import generics
from product.serializers import ProductSerializer, GroupSerializer
from product.models import ProductModel, GroupModel
from rest_framework.exceptions import NotFound

from django.db.models import Count


class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class StudentProductLessonsAPIView(generics.RetrieveAPIView):
    serializer_class = GroupSerializer

    def get_object(self):
        product_id = ProductModel.objects.get(pk=self.kwargs['product_id'])
        group_id = self.kwargs['group_id']
        group = GroupModel.objects.filter(product_id=product_id).get(id=group_id)
        if group:
            return group
        else:
            NotFound


class IndexView(ListView):
    template_name = 'product/index.html'
    model = ProductModel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_count = StudentModel.objects.count()

        products = tuple({
            'id': product.id, 
            'name': product.name,
            'start_date': product.start_date,
            'price': product.price,
            'author': product.author_id.name,
            'purchases': int(100 * StudentModel.objects.filter(products=product.id).count()/student_count) if student_count!=0 else 0,
            'max_students': product.max_users,
            'groups': GroupModel.objects.values('id', 'name').filter(product_id=product.id).annotate(total=Count('students')),
            } 
          for product in ProductModel.objects.all())


        context['product_list'] = products
        return context
          
