from django.urls import include, path
from product.views import ProductListAPIView, StudentProductLessonsAPIView

app_name = 'product'

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:product_id>/group/<int:group_id>/', StudentProductLessonsAPIView.as_view(), name='product_lessons'),
]
