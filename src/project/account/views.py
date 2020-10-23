from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from . import forms

# Register your models here.


def login(request):
    template_name = "account/login.html"
    form = forms.LoginForm(request.POST or None, use_required_attribute=False)
    
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponse(f'POST Recibido!</br>{request.POST["username"]} : {request.POST["password"]}')

    context = {
        'form': form
    }
    return render(request, template_name, context)
