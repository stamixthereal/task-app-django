from django.urls import path
from . import views
from users import views as users_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users_view.register, name='register'),
]