from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),
    path('login/', views.login, name='login'),
]