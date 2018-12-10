from django.db.models import Count, Q
from django.http import JsonResponse
from .models import *
import json
from django.utils import timezone

def curso_json(request):
    curso = Post.objects.filter(curso__iendswith='- M')\
    .values('curso')\
    .annotate(value=Count('curso'))

    lista = [
        post_serializer(item)
        for item in curso
    ]

    return JsonResponse({'cursos':lista})

def curso_not_js(request):
    curso = Post.objects.filter(curso__iendswith='- N')\
    .values('curso')\
    .annotate(value=Count('curso'))

    lista = [
        post_serializer(item)
        for item in curso
    ]
    return JsonResponse({'cursos':lista})

def confirm_sala_js(request):
    sala = Post.objects.all()\
        .values('sala')\
        .annotate(confirm=Count('confirm', filter=Q(confirm=True)))

    lista = [
        # conf_serializerS(item)
        conf_serializer(item)
        for item in sala
    ]
    return JsonResponse({'salas': lista})

def confirm_curM_js(request):
    sala = Post.objects.filter(curso__iendswith='- M')\
        .values('curso')\
        .annotate(value=Count('confirm', filter=Q(confirm=True)))

    lista = [
        # conf_serializerS(item)
        post_serializer(item)
        for item in sala
    ]
    return JsonResponse({'cursos': lista})

def confirm_curN_js(request):
    sala = Post.objects.filter(curso__iendswith='- N')\
        .values('curso')\
        .annotate(value=Count('confirm', filter=Q(confirm=True)))

    lista = [
        # conf_serializerS(item)
        post_serializer(item)
        for item in sala
    ]
    return JsonResponse({'cursos': lista})

def print_js(request):
    lista = [
        {'data':'VG-20/10/18', 'impresso':(600 * 6)},
        {'data':'VG-24/11/18', 'impresso':(800 * 6)},
        {'data':'VG-19/01/19', 'impresso':(350 * 6)},
        ]
    return JsonResponse({'print':lista})

# serialização
def post_serializer(item):
    return {'curso':item['curso'], 'quantidade':item['value']}

def conf_serializer(item):
    return {'sala':'Sala '+item['sala'], 'confirmados':item['confirm']}
