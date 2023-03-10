from django.contrib import admin
from .models import *
# Register your models here.

class TypeOfTranscationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date','item_name', 'item_price', 'item_category_id', 'item_type_id', 'item_user_id')
    list_filter = ('date', 'item_category_id', 'item_type_id', 'item_user_id')
    # list_editable = ('item_transaction_date','item_name', 'item_price', 'item_category_id', 'item_type_id', 'item_user_id')
    # list_max_show_all = 30
    list_per_page = 20
    ordering = ('-date', 'item_price')
    # raw_id_fields = ('item_category_id',)
    search_fields = ['item_name']
    search_help_text = "Поиск по наиманованию транзакции"

class BillAdmin(admin.ModelAdmin):
     list_display = ('id', 'bill_sum', 'user')
     # list_filter = ('user',)
     list_editable = ('bill_sum',)
     list_per_page = 30
     ordering = ('user', 'bill_sum')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_user_id')
    list_editable = ('category_name',)
    list_per_page = 30
    list_filter = ('category_user_id', 'category_name')
    ordering = ('category_user_id',)
    search_fields = ['category_name']

class CheckDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_name', 'check_count', 'check_price', 'check_category_id', 'date', 'check_user_id')
    list_filter = ('check_category_id', 'check_user_id')
    list_editable = ('check_category_id', 'check_name',)
    list_per_page = 30
    search_fields = ('check_name',)
    ordering = ('check_user_id', '-date')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_title', 'news_date')
    list_filter = ('news_date', )
    list_editable = ('news_title',)
    list_per_page = 30
    search_fields = ('news_title', 'news_text')
    ordering = ('news_date',)

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Type_of_transcation, TypeOfTranscationAdmin)
admin.site.register(Check_data, CheckDataAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Bill, BillAdmin)



