from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros),
    path('livros/lendo/', views.livros_lendo)
]