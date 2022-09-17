from django.http import HttpResponse
from assignment.models import Subject
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

def addCourse(request):
    if(request.method != 'POST'): return HttpResponse('Invalid method')
    subjectId = int(request.POST["subject"])
    subjectInfo = Subject.objects.get(pk=subjectId)
    if(subjectInfo is not None):
        isRegistered = subjectInfo.enroll.filter(pk=request.user.id).exists()
        isFull = subjectInfo.enroll.all().count() >= subjectInfo.max_seat
        if isRegistered:
            return HttpResponse('Already registered')
        if isFull:
            return HttpResponse('Course is full')
        subjectInfo.enroll.add(request.user)
    return redirect('view-course')

def doLogin(request):
    if(request.method != 'POST'): return HttpResponse('Invalid method')
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect('view-course')
    return redirect('login')