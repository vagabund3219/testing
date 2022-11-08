import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=80)
    def __str__(self):
        return self.category_name

class Type_of_transcation(models.Model):
    type_name = models.CharField(max_length=80)

    def __str__(self):
        return self.type_name

class Check_data(models.Model):
    check_name = models.CharField(max_length=80)
    check_count = models.FloatField()
    check_price = models.FloatField()
    check_category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    check_transaction_date = models.DateField(default=datetime.date.today())
    check_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.check_name

    class Meta:
        verbose_name = "Данные"

class Transactions(models.Model):
    item_transaction_date = models.DateField(default=datetime.date.today())
    item_name = models.CharField(max_length=80)
    item_price = models.FloatField()
    item_category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    item_type_id = models.ForeignKey(Type_of_transcation, on_delete=models.PROTECT, default=1)  # expenses incomes
    item_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)




