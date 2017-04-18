from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Student, Group

import django.contrib.auth  as auth
import json, random

#Local debugging
debug = False

#Student
numberOfQueueSet=20

#Location of JSON file.
JSONLocation = '/Content_Set'

#Views

def loginView( request ):
    return render( request, 'index.html' )

def homeView( request ):
    return render( request, 'home.html' )

def trainingView( request ):
    return render( request, 'training.html', { 'name':request.session[ 'name' ] } )

# Admin views

def adminView( request ):
    return render( request, 'admin/admin.html' )

def manageStudentView( request ):
    return render( request, 'admin/manageStudent.html', { 'stds':getStudentList() } )

def stdListView( request ):
    return render( request, 'admin/stdList.html', { 'stds':getStudentList() } )

def manageGroupView( request ):
    return render( request, 'admin/manageGroup.html', { 'groups':getGroupList() } )

#Model

def doLogin( request ):
    login_username = request.POST['Lusername']
    login_password = request.POST['Lpassword']
    row = Student.objects.filter( username=login_username, password=login_password )
    if not row :

        # Debug
        if debug:
            print( 'login fail' )
        # End debug

        return render( request, 'index.html', {'msg':"Wrong username or password"})

    # Debug
    if debug:
        print( 'login pass' )
    # End debig

    request.session['name']=row[0].name
    return render( request, 'home.html', { 'name':request.session[ 'name' ] } )

def doLogout( request ):
    return render( request, 'index.html' )

def doRegister( request ):
    register_username = request.POST['username']
    register_password = request.POST['password']
    register_name = request.POST['name']
    register_queue = generateQueues()
    register_memory = ''
    std = 0

    row = Student.objects.filter( username=register_username )
    if not row:
        return render( request, 'admin/manageStudent.html', { 'msg':"Cannot register new student username: " + register_username + "\nAlready exist!", 'stds':getStudentList() } )
    row = Student.objects.filter( name=register_name )
    if not row:
        return render( request, 'admin/manageStudent.html', { 'msg':"Cannot register new student name: " + register_name + "\nAlready exist!", 'stds':getStudentList() } )

    std = Student( username=register_username, password=register_password, name=register_name, queue=register_queue, memory=register_memory )
    std.save()

    # Debug
    if debug:
        print( 'username: ' + str( std.username ) )
        print( 'password: ' + str( std.password ) )
        print( 'name: ' + str( std.name ) )
    # End debug

    return render( request, 'admin/manageStudent.html', { 'msg':"Succesfully create student name: " + std.name, 'stds':getStudentList() } )

def deleteStd( request ):
    _std_name = request.POST['std_name']
    std = Student.objects.get( name=_std_name )
    Student.delete( std )
    # row = Student.objects.filter( name=_std_name )
    # for i in row:
    #     i.delete()
    return render( request, 'admin/manageStudent.html', { 'stds':getStudentList() } )

def addGroup( request ):
    _name = request.POST[ 'groupName' ]
    _post = request.POST[ 'ids' ]
    _visible = request.POST[ 'visible' ]

    del request.session[ 'groupName' ]
    del request.session[ 'ids' ]
    del request.session[ 'visible' ]

    row = Group.objects.filter( name=_name )

    if not row:
        return render( request, 'admin/manageGroup.html', {'msg':"Group name already exist." } )

    group = Group( name=_name, post=_post, visible=_visible )
    group.save()

    # Debug
    if debug:
        print( 'name: ' + str( group.name ) )
        print( 'post: ' + str( group.ppost ) )
        print( 'visible: ' + str( group.visible ) )
    # End debug

    render( request, 'admin/manageGroup.html')

#Misc

def getStudentList():
    return Student.objects.all()

def getGroupList():
    return Group.objects.all()

def readJson( JSONLocation, set, id_num, arr_word, arr_pos ):
    with open( JSONLocation+set+'/'+'id_'+id_num+'.json', encoding='utf-8' ) as json_data:
        decoded=json.loads( json_data.read() )
    for i in range( len( decoded[ 'id_'+id_num ] ) ):
        if decoded[ 'id_'+id_num ][ i ][ 'word' ]=='':
            0
        else:
            arr_word.append( decoded[ 'id_'+id_num ][ i ] [ 'word' ] )
            arr_pos.append( decoded[ 'id_'+id_num ][ i ][ 'pos' ] )

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
