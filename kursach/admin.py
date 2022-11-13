from django.contrib import admin
from .models import *
# Register your models here.

class TypeOfTranscationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

admin.site.register(Categories)
admin.site.register(Type_of_transcation, TypeOfTranscationAdmin)
admin.site.register(Check_data)
admin.site.register(Transactions)
admin.site.register(News)
admin.site.register(Bill)

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'transactionDate')
    list_display_links = ('id', 'transactionDate')





