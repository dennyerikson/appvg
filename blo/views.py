from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Count, Sum
from .json_print import Json_Get
from .forms import CandidatosForm
from django.db.models.sql import AggregateQuery
from datetime import date
from django.utils import timezone
from django.contrib import messages

# Create your views here.

def home(request):
    horarios = ''
    search = request.GET.get('search')

      
  

    dias = ('','Segunda-Feira','Terça-Feira','Quarta-Feira', 'Quinta-Feira','Sexta-Feira', 'Sábado')
    dia = ('','Segunda','Terça','Quarta', 'Quinta','Sexta', 'Sábado')

    # hoje = timezone.now().strftime(%A)
    hoje = "{} {}".format(dia[int(timezone.now().strftime('%w'))], timezone.now().strftime('%d/%m/%Y'))
    # print("Hoje é", timezone.now())
    # print("Dia {} nº{}".format(dias[int(timezone.now().strftime('%w'))],int(timezone.now().strftime('%w'))))
    # print("Hoje é", timezone.now().strftime('%A'))
    # print("Hoje é", timezone.now().strftime('%w'))

    """ 1º dia de Aula """
    if search:
        horarios = Horario.objects.filter(
            Q(dia=(1+int(timezone.now().strftime('%w')))),
            Q(curso=search) |
            Q(curso__contains=search)|
            Q(disciplina=search) |
            Q(disciplina__contains=search)|
            Q(sala=search) |
            Q(sala__contains=search) 
        )
    else:
        # post = Post.objects.select_related().all()
        horarios = ''
    
    # horarios = Horario.objects.filter(Q(dia__contains=(1+int(timezone.now().strftime('%w')))))

    context = {'horarios':horarios,'hoje':hoje}
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




# listaCurso = []
# lista_Curso = []

# Curso_csv = csv.reader(open('BD_HORARIO.csv'), delimiter=';')
# for [curso, periodo, disciplina, sala, dia, serie, professor] in Curso_csv:
#     listaCurso.append('{};{};{};{};{};{};{}'.format(
#         curso, periodo, disciplina, sala, dia, serie, professor)
#     )
# i=0
# while i < len(listaCurso):
#     lista_Curso.append(str(listaCurso[i]).split(';'))
#     i+=1

import csv, io
def course_upload(request):
    csv_file = ''
    template = 'blo/course_upload.html'

    prompt = {
        'order': 'Ordem do .csv'
    }
    
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "Por favor insira um arquivo .csv válido")

    print("csv get", csv_file)
    
    if csv_file:
        if request.method == "POST":

            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)

            lista_horario = []

            for [curso, periodo, disciplina, sala, dia, serie, professor] in csv.reader(
                io_string, delimiter=';', quotechar="|"):

                course = Courses.objects.get(pk=curso)

                h = Horario(
                    curso=course.name,
                    id_course_id=curso,
                    periodo=periodo,
                    disciplina=disciplina,
                    sala=sala,
                    dia=dia,
                    serie=serie,
                    professor=professor
                )
                lista_horario.append(h)

            Horario.objects.bulk_create(lista_horario)
            horarios = Horario.objects.all()
            # messages.SUCCESS(request, 'atualizado com sucesso')
            return redirect('/')
            


    
    context = {}
    return render(request, template, context)





