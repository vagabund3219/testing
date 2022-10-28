from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CheckModel)
admin.site.register(Categories)
admin.site.register(TypeOfTranscation)
admin.site.register(CheckData)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'transactionDate')
    list_display_links = ('id', 'transactionDate')



