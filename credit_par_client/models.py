from django.db import models
from client.models import Client

# Create your models here.
class Clients(models.Model):
    full_name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    creation_date=models.DateTimeField(auto_now_add=True, null=True)
    credit_debt=models.FloatField(null=True)
    amount_paid=models.FloatField(null=True)
    amount_remaining=models.FloatField(null=True)
    client=models.ForeignKey(Client, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name  
    