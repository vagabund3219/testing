from django.urls import path
from .views import *

urlpatterns = [
    path('add_transaction/', AddTransactionView.as_view(), name='add_transaction'),
    path('send-check/', send_check, name='send_check'),
    path('get_user_transactions', GetUserTransactions.as_view(), name='get_user_transactions' ),
    path('', main, name='main'),
]