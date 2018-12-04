from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Count
from .json_print import Json_Get
from .forms import CandidatosForm


# Create your views here.
def home(request):

    if request.POST:        
        get_cpf = request.POST.get('ckeckbox')

        if get_cpf:
            query = Post.objects.get(cpf=get_cpf)            
            Json_Get.cpf = get_cpf
            Json_Get.sala = query.sala

            if query.confirm == True:
                query.confirm = False
                query.save()
            else:
                query.confirm = True
                query.save()

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
    

    if request.method == 'POST':
        form = CandidatosForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.save()
            return redirect('/')
    else:
        form = CandidatosForm()



    context = {'post':post, 'total':total, 'sala':sala, 'form':form}
    return render(request, 'blo/home.html', context)


def getNome(nome):
    nome = nome.split(' ')
    nome = str(nome[0]) +' '+str(nome[-1])
    return nome

