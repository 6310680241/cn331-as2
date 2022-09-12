from django.shortcuts import render
from assignment.models import Subject

def index(request):
    subjects = Subject.objects.filter(active=1)
    return render(request, 'index.html', {
        'subjects': subjects
    })