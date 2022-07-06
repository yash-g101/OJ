from django.db import models

# Create your models here.
class Problem(models.Model):
    problem_title = models.CharField(max_length=25)
    problem_statement = models.TextField()

    def __str__(self):
        return self.problem_title
    
class Testcases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    test_input = models.TextField()
    test_output = models.TextField()

    def __str__(self):
        return self.test_input, self.test_output

VERDICT_CHOICES = (
    ("0", "Unattempted"),
    ("1", "Accepted"),
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
    submitted_code = models.TextField()
    verdict = models.CharField(max_length=40, choices=VERDICT_CHOICES)

    def __str__(self):
        return self.verdict