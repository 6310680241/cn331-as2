from django.http import HttpResponse
from assignment.models import Subject, User
from django.shortcuts import redirect
from django.contrib.auth import login
import hashlib

def addCourse(request):
    subjectId = int(request.POST["subject"])
    subjectInfo = Subject.objects.get(pk=subjectId)
    return HttpResponse(f"POST -> {subjectInfo.code} {subjectInfo.name}")

def doLogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.filter(username=username).filter(password=hashlib.md5(password.encode()).hexdigest())
    if len(user) >= 1:
        login(request, user[0])
        return HttpResponse("Completed")
        # return redirect('index')
    return HttpResponse("Failure")
    # return redirect('login', error=1)