from django.shortcuts import render, HttpResponse
from .script_folder import checkScript
from .forms import CheckForm, AddCheck

def index(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['checkImg'].read()
        response_data = checkScript.send_check(file)
        if response_data != None:
            return render(request, 'kursach/responsed.html', {'response_data': response_data})
        else:
            form = CheckForm()
            error = 'This is not check'
            return render(request, 'kursach/index.html', {'form': form, 'error': error})
    else:
        form = CheckForm()
    return render(request, 'kursach/index.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = AddCheck(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = AddCheck()
    return render(request, 'kursach/add_transaction.html', {'form': form})
