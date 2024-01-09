from django.contrib import admin
from django.urls import path
from RecEngine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name="welcome"),
    path('login/', views.login, name="login"),
    path('about/', views.about, name="about"),
    path('logout/', views.logout, name="logout"),
    path('home', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('result/', views.result, name="receng-result"),
    path('<str:movie_id>/', views.detail, name="detail"),
    

]
