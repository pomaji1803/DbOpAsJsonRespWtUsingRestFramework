from django.db import models

class ProductModel(models.Model):
    No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50,unique=True)
    Price = models.FloatField()
    Quantity = models.IntegerField()