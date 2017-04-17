from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    #Views
    url(r'^$', views.loginView, name='login'),
    url(r'^register', views.registerView, name='register'),
    url(r'^stdList', views.stdListView, name='stdList'),
    url(r'^home', views.homeView, name='home'),
    url(r'^training', views.trainingView, name='training'),
    url(r'^appAdmin', views.adminView, name='appAdmin'),
    url(r'^group', views.groupView, name='group'),
    url(r'^training', views.trainingView, name='training'),
    #Actions
    url(r'^doLogin', views.doLogin, name='doLogin'),
    url(r'^doRegister', views.doRegister, name='doRegister'),
    url(r'^deleteStd', views.deleteStd, name='deleteStd'),
    url(r'^logout', views.doLogout, name='doLogout'),
]
