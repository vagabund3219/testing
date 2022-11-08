from django import forms
from .models import Categories, Check_data, Type_of_transcation, Transactions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class Add_check(forms.Form):
#     checkImg = forms.ImageField()

class Add_check_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['check_category_id']

    checkImg = forms.ImageField()
    check_category_id = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="(Nothing)")


class Add_transaction_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [ 'item_transaction_date', 'item_name', 'item_price', 'item_category_id', 'item_type_id']
    item_type_id = forms.ModelChoiceField(queryset=Type_of_transcation.objects.all(), empty_label="(Nothing)")
    item_transaction_date = forms.DateField()
    item_category_id = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="(Nothing)")
    item_name = forms.CharField()
    item_price = forms.FloatField()

class User_register_form(UserCreationForm):
    username  = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
