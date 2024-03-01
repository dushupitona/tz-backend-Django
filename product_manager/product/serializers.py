from rest_framework import serializers
from product.models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = ['id']
class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    author = serializers.CharField(source='author_id.name')
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'start_date', 'price', 'min_users', 'max_users', 'author', 'lessons')
    def get_lessons(self, obj):
        return obj.lessonmodel_set.count()

# -------------------------------------------------------------------------------------------

class LessonShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = ['id', 'name', 'video_url']


class ProductShowSerializer(serializers.ModelSerializer):
     class Meta:
         model = ProductModel
         fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):
    lessons = LessonShowSerializer(many=True)
    product_id = ProductShowSerializer()
    students = StudentSerializer(many=True)
    class Meta:
            model = GroupModel
            fields = ['id', 'name',     'product_id', 'students', 'lessons']

