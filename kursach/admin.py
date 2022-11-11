from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Categories)
admin.site.register(Type_of_transcation)
admin.site.register(Check_data)
admin.site.register(Transactions)
admin.site.register(News)

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'transactionDate')
    list_display_links = ('id', 'transactionDate')



