from django.shortcuts import render
from .models import *
from django.db.models import Q, Count

# Create your views here.
def home(request):

    search = request.GET.get('search')

    if search:
        post = Post.objects.filter(
            Q(cpf=search) |
            Q(nome__contains=search)|
            Q(sala=search)
        )
    else:
        post = Post.objects.all()

    total = Post.objects.all().count()

    # minha query onde obtenho os dados das salas
    sala = Post.objects.all()\
        .values('sala')\
        .annotate(value_sala=Count('sala'), value_cpf=Count('cpf') )
    print(sala)

    context = {'post':post, 'total':total, 'sala':sala}
    return render(request, 'blo/home.html', context)
