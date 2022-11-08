from django import forms
from .models import Categories, Check_data, Type_of_transcation, Transactions
# from django.contrib.auth.models import User
# class Add_check(forms.Form):
#     checkImg = forms.ImageField()

class Add_check_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['check_category_id']

    checkImg = forms.ImageField(label='Чек', widget=forms.FileInput(attrs={'class': 'form-control', 'id': "formFile"}))
    check_category_id = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="(Nothing)", label='Категория', widget=forms.Select(attrs={'class': 'form-control'}))


class Add_transaction_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [ 'item_transaction_date', 'item_name', 'item_price', 'item_category_id', 'item_type_id']
        widgets = {
            'item_transaction_date': forms.DateInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_price': forms.TextInput(attrs={'class': 'form-control'}),
            'item_category_id': forms.Select(attrs={'class': 'form-control'}),
            'item_type_id': forms.Select(attrs={'class': 'form-control'})
        }


