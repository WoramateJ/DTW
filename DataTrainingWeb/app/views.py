from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Student

import django.contrib.auth  as auth
import json

# Create your views here.

#Local debugging
debug = False

#Location of JSON file.
JLocation = ''

#Views

def loginView( request ):
    return render( request, 'index.html' )

def registerView( request ):
    return render( request, 'register.html' )

def stdListView( request ):
    return render( request, 'stdList.html', { 'stds':getStudentList() } )

def homeView( request ):
    return render( request, 'home.html', {'no_group':no_group} )

#Logical

def doLogin( request ):
    username = request.POST['username']
    password = request.POST['password']
    row = Student.objects.filter( username=username, password=password )
    if not row :
        if debug:
            print( 'login fail' )
        return render( request, 'register.html')
    if debug:
        print( 'login pass' )
    return render( request, 'home.html' )

def doRegister( request ):
    username = request.POST['username']
    password = request.POST['password']
    passwordCheck = request.POST['passwordCheck']
    name = request.POST['name']
    std = 0
    if password == passwordCheck:
        std = Student( username=username, password=password, name=name )
        std.save()
    if debug:
        print( 'username: ' + str( std.username ) )
        print( 'password: ' + str( std.password ) )
        print( 'name: ' + str( std.name ) )
    return render( request, 'index.html' )

def getStudentList():
    return Student.objects.all()

def loadJson( id_num ):
    return 0