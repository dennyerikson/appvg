from django.db import models

# Create your models here.
class Post(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)

    def __str__(self):
        return self.cpf
    
