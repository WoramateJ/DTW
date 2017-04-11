from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^doLogin', views.doLogin, name='doLogin'),
    url(r'^register', views.registerView, name='register'),
    url(r'^doRegister', views.doRegister, name='doRegister'),
    url(r'^stdList', views.stdListView, name='stdList'),
]
