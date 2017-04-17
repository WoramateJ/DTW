from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Student

import django.contrib.auth  as auth
import json, random

#Local debugging
debug = False

#Student
numberOfQueueSet=20

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
    return render( request, 'home.html' )

def trainingView( request ):
    return render( request, 'training.html' )

def adminView( request ):
    return render( request, 'admin.html' )

def groupView( request ):
    return render( request, 'group.html' )

def trainingView( request ):
    return render( request, 'training.html' )

#Model

def doLogin( request ):
    _username = request.POST['username']
    _password = request.POST['password']
    row = Student.objects.filter( username=_username, password=_password )
    if not row :

        # Debug
        if debug:
            print( 'login fail' )
        # End debug

        return render( request, 'register.html')

    # Debug
    if debug:
        print( 'login pass' )
    # End debig

    request.session['name']=row[0].name
    return render( request, 'home.html', { 'name':request.session[ 'name' ] } )

def doLogout( request ):
    return render( request, 'index.html' )

def doRegister( request ):
    _username = request.POST['username']
    _password = request.POST['password']
    _passwordCheck = request.POST['passwordCheck']
    _name = request.POST['name']
    _queue = generateQueues()
    _memory = ''
    std = 0
    if _password == _passwordCheck:
        std = Student( username=_username, password=_password, name=_name, queue=_queue, memory=_memory )
        std.save()

    # Debug
    if debug:
        print( 'username: ' + str( std.username ) )
        print( 'password: ' + str( std.password ) )
        print( 'name: ' + str( std.name ) )
    # End debug

    return render( request, 'index.html' )

def deleteStd( request ):
    _std_name = request.POST['std_name']
    std = Student.objects.get( name=_std_name )
    Student.delete( std )
    return render( request, 'stdList.html' )

#Misc

def getStudentList():
    return Student.objects.all()

def loadJson( id_num ):
    return 0

def generateQueue():
    l = [[0,True],[1,True],[2,True],[3,True],[4,True],[5,True],[6,True],[7,True],[8,True],[9,True],[10,True],[11,True],[12,True],[13,True],[14,True],[15,True],[16,True],[17,True],[18,True],[19,True]]
    tmp = ''
    count = 0
    while( True ):
        r = random.randint( 0, 19 )
        if l[r-1][1]:
            l[r-1][1] = False
            if r<10:
                tmp = tmp+'0'+str( r )
            else:
                tmp = tmp+str( r )
            count = count+1
        if count == 20:
            break
    return tmp

def generateQueues():
    n = numberOfQueueSet
    tmp = ''
    i = 0
    while( i<n ):
        tmp = tmp+generateQueue()
        i=i+1
        if n-i!=0:
            tmp=tmp+','
    return tmp
