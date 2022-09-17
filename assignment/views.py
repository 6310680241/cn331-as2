from http.client import HTTPResponse
from django.shortcuts import render, redirect
from assignment.models import Subject
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from assignment.controller import doLogin, addCourse

def logout_index(request):
    logout(request)
    return redirect('login')

def login_index(request):
    print(request.user)
    if(request.method != "POST"): return render(request, 'login.html')
    return doLogin(request)

@login_required(login_url='/login')
def index(request):
    if(request.method != "POST"): return addCourse(request)
    subjects = Subject.objects.filter(active=1)
    return render(request, 'index.html', {
        'subjects': subjects
    })