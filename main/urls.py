from django.urls import path
from . import views
from main.views import TaskDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_ticket/', views.new_task, name='new_task'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail')
]