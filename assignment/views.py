from django.shortcuts import render, redirect
from assignment.models import Subject
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from assignment.controller import doLogin, addCourse

def logout_index(request):
    logout(request)
    return redirect('login')

def login_index(request):
    if(request.method == "GET"): return render(request, 'login.html')
    return doLogin(request)

@login_required(login_url='/login')
def course_index(request):
    if(request.method == "GET"):
        subjects = Subject.objects.filter(active=1)
        enrolled = [subject for subject in subjects.filter(enroll__in=[request.user.id]) if subject.enroll.all().count() < subject.max_seat]
        total_credit = sum([enroll.credit for enroll in enrolled])
        return render(request, 'index.html', {
            'enrolled': enrolled,
            'subjects': subjects.exclude(enroll__in=[request.user.id]),
            'all_subject': subjects if request.user.is_staff else [],
            'total_credit': total_credit
        })
    return addCourse(request)

def course_delete(request, id, user_id = None):
    subjects = Subject.objects.get(pk=id)
    user = User.objects.get(pk=user_id if user_id is not None and request.user.is_staff else request.user.id)
    subjects.enroll.remove(user)
    return redirect('view-course')