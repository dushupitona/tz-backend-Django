from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.db.models import Count, Sum, Avg, Max, Min
from django.dispatch import receiver
from product.models import GroupModel, StudentModel, ProductModel


@receiver(m2m_changed, sender=StudentModel.products.through)
def my_m2m_changed_handler(sender, instance, action, **kwargs):
    if action == 'post_add':
        student_products = instance.products.all()
        for product in student_products:
            # min_users = product.min_users
            max_users = product.max_users
            product_groups = GroupModel.objects.all().filter(product_id = product.id)
            for group in product_groups:
                check = instance.groupmodel_set.filter(product_id=product.id)
                if group.students.count() < max_users and check.count() != 1:
                    group.students.add(instance)
                    break
                elif group == product_groups.last():
                    print(f'Группы для продукта {product.name} переполнены! Необходимо добавить новую группу или расширить максимальное кол-во человек в группе.')
                    

