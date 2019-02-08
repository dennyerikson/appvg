from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Count, Sum
from .json_print import Json_Get
from .forms import CandidatosForm
from django.db.models.sql import AggregateQuery

# Create your views here.

def home(request):
    horarios = ''
    search = request.GET.get('search')

    """ 1º dia de Aula """
    if search:
        horarios = Horario.objects.filter(
            Q(curso=search) |
            Q(curso__contains=search)|
            Q(disciplina=search) |
            Q(disciplina__contains=search)|
            Q(dia__contains=search)|
            Q(sala=search) |
            Q(sala__contains=search) 
        )
    else:
        # post = Post.objects.select_related().all()
        horarios = ''

    context = {'horarios':horarios}
    return render(request, 'blo/home.html', context)

    # if request.POST:        
    #     get_cpf = request.POST.get('ckeckbox')

    #     if get_cpf:
    #         query = Post.objects.get(cpf=get_cpf)            
    #         Json_Get.cpf = get_cpf
    #         Json_Get.sala = query.sala

    #         if query.confirm == True:
    #             query.confirm = False
    #             query.save()
    #         else:
    #             query.confirm = True
    #             query.save()

    # search = request.GET.get('search')

    #vestibular
    # if search:
    #     post = Post.objects.filter(
    #         Q(cpf=search) |
    #         Q(nome__contains=search)|
    #         Q(sala=search) |
    #         Q(curso__contains=search) 
    #     )
    # else:
    #     # post = Post.objects.select_related().all()
    #     post = ''

    # total = Post.objects.all().count()
    

    # total = Post.objects.all().count()

    #minha query onde obtenho os dados das salas
    # sala = Post.objects.all()\
    #     .values('sala')\
    #     .annotate(
    #         value_cpf=Count('cpf'),
    #         value_confirm=Count('confirm', filter=Q(confirm=True)),
    #     )
    # print(sala)
    # total_confirm = Post.objects.filter(confirm=True).count()     


    # if request.method == 'POST':
    #     form = CandidatosForm(request.POST)
    #     if form.is_valid():
    #         q = form.save(commit=False)
    #         q.save()
    #         return redirect('/')
    # else:
    #     form = CandidatosForm()



    # context = {'horario':horario, 'total':total, 'sala':sala, 'form':form, 'total_confirm':total_confirm}
    # return render(request, 'blo/home.html', context)

    


def getNome(nome):
    nome = nome.split(' ')
    nome = str(nome[0]) +' '+str(nome[-1])
    return nome

def post_graphs(request):
    return render(request, 'blo/post_graphs.html')

def confirm_graphs(request):
    return render(request, 'blo/confirm_graphs.html')

def print_graphs(request):
    return render(request, 'blo/print_graphs.html')