from django.db import models

# Create your models here.
class Client(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)
    product_name=models.CharField(max_length=200, null=True)
    product_quantity=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
