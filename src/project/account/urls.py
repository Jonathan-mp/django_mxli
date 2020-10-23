from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'account'

urlpatterns = [
    url(r'^login$', views.login, name='account_login'),
]