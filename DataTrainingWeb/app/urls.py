from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    #Views
    url(r'^$', views.loginView, name='login'),
    url(r'^managestudent', views.manageStudentView, name='manageStudent'),
    url(r'^stdlist', views.stdListView, name='stdList'),
    url(r'^home', views.homeView, name='home'),
    url(r'^training', views.trainingView, name='training'),
    url(r'^appadmin', views.adminView, name='appAdmin'),
    url(r'^managegroup', views.manageGroupView, name='manageGroup'),
    url(r'^training', views.trainingView, name='training'),
    #Actions
    url(r'^dologin', views.doLogin, name='doLogin'),
    url(r'^doregister', views.doRegister, name='doRegister'),
    url(r'^deletestd', views.deleteStd, name='deleteStd'),
    url(r'^logout', views.doLogout, name='doLogout'),
    url(r'^addgroup', views.addGroup, name='addGroup'),
]
