from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cidade = models.CharField(max_length=100)
    endereco = models.TextField()
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

