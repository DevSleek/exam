from django.db import models
from utility.models import BaseMode


class Product(BaseMode):
    name = models.CharField()
    code = models.CharField()

    def __str__(self):
        return self.name


class Material(BaseMode):
    name = models.CharField()

    def __str__(self):
        return self.name


class ProductMaterial(BaseMode):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_material')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='product_material')
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.product} - {self.material} - {self.quantity}'


class Warehouse(BaseMode):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='warehouse')
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.material}'

