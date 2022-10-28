from django import forms
from .models import CheckModel, Categories, CheckData, TypeOfTranscation

class CheckForm(forms.ModelForm):
    class Meta:
        model = CheckModel
        fields = ['checkImg']

class AddCheck(forms.ModelForm):
    class Meta:
        model = CheckData
        fields = ['transactionDate', 'typeId', 'itemCategoryId', 'itemUniq', 'itemName', 'itemCount', 'itemPrice']
    typeId = forms.ModelChoiceField(queryset=TypeOfTranscation.objects.all(), empty_label="(Nothing)")
    transactionDate = forms.DateField()
    itemCategoryId = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="(Nothing)")
    itemUniq = forms.CharField()
    itemName = forms.CharField()
    itemCount = forms.FloatField()
    itemPrice = forms.FloatField()
