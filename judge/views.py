from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem, Submissions, Testcases
import os, filecmp

def index(request):
    problem_list = Problem.objects.all()
    return render(request, "judge/index.html", {'problem_list': problem_list})

def tests(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'judge/testcases.html', {'problem': problem})

def answers(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'judge/submissions.html', {'problem': problem})

def submit(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    f = request.FILES('sol')
    with open('/Users/Yash/Desktop/Output/sol.cpp', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)
    os.system('g++ /Users/Yash/Desktop/folder/sol.cpp')
    os.system('./a.out < /Users/Yash/Desktop/folder/inp.txt > /Users/Yash/Desktop/folder/out.txt')

    out1 = '/Users/Yash/Desktop/folder/out.txt'
    out2 = 'Users/Yash/Desktop/folder/actual_out.txt'
    if(filecmp.cmp(out1, out2, shallow=False)):
        verdict = "Accepted"
    else:
        verdict = "WA"
    
    submission = Submissions()
    submission.problem = Problem.objects.get(pk=problem_id)
    submission.verdict = verdict
    submission.submitted_code = '/Users/Yash/Desktop/folder/sol.cpp'
    submission.language = "C++"
    submission.save()

    return HttpResponseRedirect(reverse('judge:leaderboard'))

def leaderboard(request):
    submissions = Submissions.objects.all()
    return render(request, 'judge/leaderboard.html', {'submissions': submissions})