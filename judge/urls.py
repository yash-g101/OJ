from django.urls import path

from . import views

app_name = 'judge'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:problem_id>/', views.tests, name='tests'),
    path('<int:problem_id>/submit', views.answers, name='answer'),
]