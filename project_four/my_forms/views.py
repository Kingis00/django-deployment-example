from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'my_forms/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print(f'Name: {form.cleaned_data["name"]}')
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])

    return render(request, 'my_forms/form_page.html', {'form': form})
