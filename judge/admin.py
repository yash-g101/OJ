from django.contrib import admin
from .models import Problem, Testcases, Submission

# Register your models here.
admin.site.register(Problem)
admin.site.register(Testcases)
admin.site.register(Submission)
