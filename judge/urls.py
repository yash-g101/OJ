from django.urls import path

from . import views

app_name = 'judge'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('problems/', views.problems, name='problems'),
    path('logout/', views.user_logout, name='logout'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('problems/<int:problem_id>/result/', views.submit_problem, name='submission'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]