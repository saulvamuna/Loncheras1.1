from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('students/', views.students, name="students"),
    path('registerStudent/', views.registerStudent, name="registerStudent"),
    path('profile/', views.profile, name="profile"),
]