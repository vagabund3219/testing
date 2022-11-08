from django.urls import path
from .views import *

urlpatterns = [
    path('add_transaction/', add_transaction, name='add_transaction'),
    path('send-check/', send_check, name='send_check'),
    path('', main, name='main'),
]