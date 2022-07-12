from distutils.command.upload import upload
from django.db import models
import os

class Problem(models.Model):
    title = models.CharField(max_length=100)
    problem_statement = models.TextField()
    code = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=100)

    def get_upload_path(instance, filename):
        return os.path.join("uploads/solution/p%d" % instance.problem_id, filename)

    submission_time = models.DateTimeField()
    submitted_code = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.verdict

class Testcases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def get_upload_path_input(instance, filename):
        return os.path.join("uploads/input/p%d" % instance.problem_id, filename)

    def get_upload_path_output(instance, filename):
        return os.path.join("uploads/output/p%d" % instance.problem_id, filename)


    input = models.FileField(upload_to=get_upload_path_input)
    output = models.FileField(upload_to=get_upload_path_output)