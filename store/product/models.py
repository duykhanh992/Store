from django.db import models

# Create your models here.


class Products(models.Model):
    CHOICES = [(i, i) for i in range(10)]
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=25)
    product_name = models.CharField(max_length=25)
    product_quantity = models.IntegerField(choices=CHOICES)
    created_at = models.DateField(auto_now_add=True)

