from django.http import JsonResponse
from .models import Livro

def listar_livros(request):
    livros = list(Livro.objects.values())
    return JsonResponse(livros, safe=False)

def livros_lendo(request):
    livros = list(Livro.objects.filter(status='LENDO').values())
    return JsonResponse(livros, safe=False)