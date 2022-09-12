from django.shortcuts import render, redirect
from assignment.models import Subject
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'home.html')

def show_subj(request):
    subjects = Subject.objects.filter(active=1)
    return render(request, 'index.html', {
        'subjects': subjects,
    })

def login_view(request):
	if request.method == "POST":

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('view-course')
		else:
			return redirect('login')	

	else:
		return render(request, 'login.html', {})

def logout_view(request):
	logout(request)
	return redirect('home')