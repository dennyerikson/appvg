from django.db import models

# Create your models here.
class Post(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    curso = models.CharField(max_length=150)
    confirm = models.BooleanField(
        default=False
        )

    def __str__(self):
        return self.sala

class Candidatos(models.Model):
    PERIODO = (
        ('1', 'Matutino'),
        ('2', 'Noturno'),
    )

    EMAILS = (
        ('1','gmail.com'),
        ('2','hotmail.com'),
        ('3','outlook.coom'),
        ('4','ig.com'),
        ('5','yahool.com.br'),
    )

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    email_opc = models.CharField(max_length=2, choices=EMAILS)
    data_nasc = models.CharField(max_length=150)
    data_hist = models.DateField()
    rg = models.CharField(max_length=14)
    tel = models.CharField(max_length=10)
    cel = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    endereco_n = models.CharField(max_length=8)
    endereco_cep = models.CharField(max_length=15)
    endereco_cid = models.CharField(max_length=100)
    endereco_est = models.CharField(max_length=50)
    curso_opc1 = models.CharField(max_length=2)
    period_opc1 = models.CharField(max_length=2, choices=PERIODO)
    curso_opc2 = models.CharField(max_length=2)
    period_opc2 = models.CharField(max_length=2, choices=PERIODO)
    opc_info = models.BooleanField(default=False)

    def __str__(self):
        return self.cpf

class Cursos(models.Model):
    cod_curso = models.CharField(max_length=10)
    nome_curso = models.CharField(max_length=150)
