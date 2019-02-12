from django import template
from blo.models import Post

register = template.Library()

@register.filter
def display_name_tag(nome):
    nome = nome.split(' ')
    nome = str(nome[0]) +' '+str(nome[-1])
    return nome

@register.simple_tag
def display_curses_tag(valor):

    courses = Courses.objects.filter(value=valor).order_by('name')
    if courses:
        return courses
    return False

def DIA_SEMANA():
    DIAS = (
        ('2', 'Segunda-feira'),
        ('3', 'Terça-feira'),
        ('4', 'Quarta-feira'),
        ('5', 'Quinta-feira'),
        ('6', 'Sexta-feira'),
        ('7', 'Sábado'),
    )
    return DIAS


@register.simple_tag
def display_dia_tag(value):
    return dict(DIA_SEMANA()).get(value,'')