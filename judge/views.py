from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm
import os, filecmp

from .models import Problem, Submission, Testcases

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) # checks for authentication of the user automatically

        if user:
                login(request, user) # django inbuilt function for login
                return HttpResponseRedirect(reverse('judge:problems'))
        else:
            return render(request, 'judge/login.html', {'message': "Username and Password are incorrect"})
    else:
        return render(request,'judge/login.html',{})


def register(request):
    user_form = RegForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid(): # Check the form validity

            user = user_form.save() # Saving the data to database
            user.set_password(user.password)  # set_password method used to save the password in hashed form
            user.save()  # Saved the hashed password and user
            return HttpResponseRedirect(reverse('judge:login'))

        else:
            print(user_form.errors)
    return render(request, 'judge/register.html', {'user_form': user_form})

def user_logout(request):
    logout(request) # django inbuilt function for logout
    return HttpResponseRedirect(reverse('judge:login'))

def problems(request):
    problems_list = Problem.objects.all()
    context = {'problems_list': problems_list}
    return render(request, 'judge/index.html', context)

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'judge/detail.html', {'problem': problem})

def submit_problem(request, problem_id):
    f = request.FILES['submission']
    with open('C:/Users/Yash/Desktop/OJ/online_judge/folder/solution/submission%d.cpp' % problem_id, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)
    os.system('g++ C:/Users/Yash/Desktop/OJ/online_judge/folder/solution/submission%d.cpp' % problem_id)
    os.system('a.exe < C:/Users/Yash/Desktop/OJ/online_judge/folder/input/input.txt > C:/Users/Yash/Desktop/OJ/online_judge/folder/output/output.txt')

    out1 = 'C:/Users/Yash/Desktop/OJ/online_judge/folder/output/output.txt'
    out2 = 'C:/Users/Yash/Desktop/OJ/online_judge/folder/output/actual_out.txt'

    if(filecmp.cmp(out1, out2, shallow=False)):
        verdict = 'Accepted'
    else:
        verdict = 'Wrong Answer'
    
    submission = Submission()
    submission.problem = Problem.objects.get(pk=problem_id)
    submission.verdict = verdict
    submission.submission_time = timezone.now()
    submission.submitted_code = 'C:/Users/Yash/Desktop/OJ/online_judge/folder/solution/submission%d.cpp' % problem_id
    submission.save()

    return HttpResponseRedirect(reverse('judge:leaderboard'))

def leaderboard(request):
    submissions = Submission.objects.all()
    return render(request, 'judge/leaderboard.html', {'submissions': submissions})

