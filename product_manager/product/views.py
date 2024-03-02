from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import generics
from product.serializers import ProductSerializer, GroupSerializer
from product.models import ProductModel, GroupModel
from rest_framework.exceptions import NotFound


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


def index(request):
    return render(request, 'product/index.html')
          
