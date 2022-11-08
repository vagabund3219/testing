from django.shortcuts import render, HttpResponse, redirect
from .script_folder import checkScript
from .forms import Add_check_form, Add_transaction_form, User_register_form
from .models import Check_data
from django.contrib import messages
from django.views.generic import ListView, CreateView

def send_check(request):
    template = 'kursach/index.html'
    if request.method == 'POST' and request.FILES:
        form = Add_check_form(request.POST, request.FILES)
        file = request.FILES['checkImg'].read()
        response_data = checkScript.send_check(file)
        if response_data != None and form.is_valid():
            for item in response_data:
                to_db = Check_data(check_name=item['item'], check_count=item['count'], check_price=item['price'], check_category_id=form.cleaned_data['check_category_id'])
                to_db.save()
            return render(request, 'kursach/responsed.html', {'response_data': response_data})
        else:
            form = Add_check_form()
            error = 'This is not check'
            return render(request, template, {'form': form, 'error': error})
    else:
        form = Add_check_form()
    return render(request, template, {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = Add_transaction_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = Add_transaction_form()
    return render(request, 'kursach/add_transaction.html', {'form': form})

def main(request):
    return render(request, 'kursach/base.html')

def register(request):
    if request.method == 'POST':
        form = User_register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = User_register_form()
    return render(request, 'kursach/register.html', {'form': form})
def login(request):
    return render(request, 'kursach/login.html')
