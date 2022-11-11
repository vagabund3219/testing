from django.shortcuts import render, HttpResponse, redirect
from django.utils import dateformat
from kursovoiProekt import settings
from .script_folder import checkScript
from .forms import Add_check_form, Add_transaction_form, AddNewCategory
from .models import Check_data, Transactions, Categories, News
from django.views.generic import ListView, CreateView, DetailView



class NewsList(ListView):
    model = News

class NewsDetail(DetailView):
    model = News

class GetUserTransactions(ListView):
    model = Transactions
    def get_queryset(self):
        return Transactions.objects.filter(item_user_id = self.request.user.id)

class AddTransactionView(CreateView):
    model = Transactions
    template_name_suffix = '_create_form'
    form_class = Add_transaction_form

    def form_valid(self, form):
        form.instance.item_user_id = self.request.user
        return super(AddTransactionView, self).form_valid(form)

class ViewCheck(ListView):
    model = Check_data
    def get_queryset(self):
        return Check_data.objects.filter(check_user_id=self.request.user.id)

class AddNewCategory(CreateView):
    model = Categories
    template_name_suffix = '_create_form'
    form_class = AddNewCategory

    def form_valid(self, form):
        form.instance.item_user_id = self.request.user
        return super(AddNewCategory, self).form_valid(form)

def send_check(request):
    template = 'kursach/index.html'
    if request.method == 'POST' and request.FILES:
        form = Add_check_form(request.POST, request.FILES)
        file = request.FILES['checkImg'].read()
        response_data = checkScript.send_check(file)
        if response_data != None and form.is_valid():
            for item in response_data:
                to_db = Check_data(check_name=item['item'], check_count=item['count'], check_price=item['price'], check_category_id=form.cleaned_data['check_category_id'], check_user_id = request.user)
                to_db.save()
            return render(request, 'kursach/responsed.html', {'response_data': response_data})
        else:
            form = Add_check_form()
            error = 'This is not check'
            return render(request, template, {'form': form, 'error': error})
    else:
        form = Add_check_form()
    return render(request, template, {'form': form})

def main(request):
    return render(request, 'kursach/news_list.html')


