from django.db import models

class Livro(models.Model):
    STATUS_CHOICES = [
        ('LIDO', 'Lido'),
        ('LENDO', "Lendo"),
        ('QUERO LER', 'Quero ler'),
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='LIDO')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo