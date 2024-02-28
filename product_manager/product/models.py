from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    price = models.IntegerField()
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    author_id = models.ForeignKey(to=AuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LessonModel(models.Model):
    name = models.CharField(max_length=128)
    video_url = models.URLField()
    product_id = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentModel(models.Model):
    name = models.CharField(max_length=128)
    products = models.ManyToManyField(to=ProductModel)

    def __str__(self):
        return self.name


class GroupModel(models.Model):
    name = models.CharField(max_length=128)
    product_id = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(to=LessonModel)
    students = models.ManyToManyField(to=StudentModel)

    def __str__(self):
        return self.name
