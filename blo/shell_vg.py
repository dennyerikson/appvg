import csv
from blo.models import Post, Horario

# vg_list = []

# with open('VG24.csv','r') as f:
#     r = csv.DictReader(f)

#     for [r_cpf] in r:
#         vg_list.append('{}'.format(r_cpf))
    
#     f.close()

# print(vg_list)


listaCurso = []
lista_Curso = []

Curso_csv = csv.reader(open('BD_HORARIO.csv'), delimiter=';')
for [curso, periodo, disciplina, sala, dia, serie, professor] in Curso_csv:
    listaCurso.append('{};{};{};{};{};{};{}'.format(
        curso, periodo, disciplina, sala, dia, serie, professor)
    )
i=0
while i < len(listaCurso):
    lista_Curso.append(str(listaCurso[i]).split(';'))
    i+=1

lista = []
lista_stt = []

dados_csv = csv.reader(open('p.csv'), delimiter=';')
for [curso, periodo, disciplina, sala, dia, serie, professor] in dados_csv:
    lista.append('{};{};{};{};{};{};{}'.format(
        curso, periodo, disciplina, sala, dia, serie, professor)
    )
i=0
while i < len(lista):
    lista_stt.append(str(lista[i]).split(';'))
    i+=1


i=0
while i < len(lista_stt):
# while i < 3:
    index = lista_stt[i]
    index[0] = index[0]

    indexCurso = lista_Curso[i]
    indexCurso[0] = indexCurso[0]

    try:
        query = Horario.objects.create(
        curso=indexCurso[0],
        periodo=index[1],
        disciplina=index[2],
        sala=index[3],
        dia=index[4],
        serie=index[5],
        professor=index[6]
        )
        print('index: {} Sucess! - Curso:{} | dia:{} '.format(i, indexCurso[0], index[4]))
    except:
        print('index: {} Não cadastrado! - Curso:{} | dia:{} '.format(i, indexCurso[0], index[4]))
    i+=1
# terminal$ python manage.py shell < app_vg/blo/shell_vg.py
# no projeto no terminal$ python manage.py shell < blo/shell_vg.py