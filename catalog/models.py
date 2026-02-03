from django.db import models
from users.models import CustomUser

# Create your models here.
class Category(models.Model):
     name_category = models.CharField(max_length=150, verbose_name='Наименование')
     description_category = models.TextField()

     def __str__(self):
         return self.name_category

     class Meta:
         verbose_name = 'категория'
         verbose_name_plural = 'категории'
         ordering = ['name_category']


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Наименование')
    description_product = models.TextField()
    image_product = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category_product = models.ForeignKey(Category, models.CASCADE, related_name='products')
    price_product = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    publication_status = models.BooleanField(default=False, null=True, blank=True)
    owner = models.ForeignKey(CustomUser,verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name_product']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
