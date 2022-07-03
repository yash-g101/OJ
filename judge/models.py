from django.db import models

# Create your models here.
class Problem(models.Model):
    problem_title = models.CharField(max_length=25)
    problem_statement = models.TextField()
    
class Testcases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    test_input = models.TextField()
    test_output = models.TextField()

VERDICT_CHOICES = (
    ("0", "Unattempted"),
    ("1", "Correct Answer"),
    ("2", "WA"), 
    ("3", "TLE"),
    ("4", "CTE"),
    ("5", "RTE"),
)

LANGUAGE_CHOICES = (
    ("C", "C"),
    ("C++", "C++"),
    ("Python3", "Python3"),
    ("Java", "Java"),
)

class Submissions(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default="C++")
    submission = models.TextField()
    verdict = models.CharField(max_length=40, choices=VERDICT_CHOICES)