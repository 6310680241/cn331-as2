from django.http import HttpResponse
from assignment.models import Subject

def addCourse(request):
    if request.method == "POST":
        subjectId = int(request.POST["subject"])
        subjectInfo = Subject.objects.get(pk=subjectId)
        return HttpResponse(f"POST -> {subjectInfo.code} {subjectInfo.name}")
    return HttpResponse("GET!")