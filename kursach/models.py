from django.db import models

# Create your models here.

class CheckModel(models.Model):
    checkImg = models.ImageField(upload_to='images/%Y/%m/%d/')

class Categories(models.Model):
    categoryName = models.CharField(max_length=80)
    def __str__(self):
        return self.categoryName

class TypeOfTranscation(models.Model):
    typeName = models.CharField(max_length=80)
    def __str__(self):
        return self.typeName

class CheckData(models.Model):
    itemUniq = models.CharField(max_length=80)
    itemName = models.CharField(max_length=80)
    itemCount = models.FloatField()
    itemPrice = models.FloatField()
    itemCategoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    itemTypeId = models.ForeignKey(TypeOfTranscation, on_delete=models.PROTECT)  # expenses incomes
    itemTransactionDate = models.DateField()

    def __str__(self):
        return self.itemName

    class Meta:
        verbose_name = "Данные"

# class Transactions(models.Model):
#     itemCategoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     checkId = models.ForeignKey(CheckData, on_delete=models.CASCADE)
#     typeId = models.ForeignKey(TypeOfTranscation, on_delete=models.PROTECT)  # expenses incomes
#     transactionDate = models.DateField()


