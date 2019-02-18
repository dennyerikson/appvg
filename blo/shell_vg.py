import csv
from blo.models import Post, Horario, Courses

def integer(texto):
    lista = []
    numero = 2
    for i in range(2,30):
        lista.append("{}".format(i))
    print(texto)
    if texto in lista:
        inteiro = lista.index(texto)
        numero = int(lista[inteiro])
    
    # if numero == 0:
    #     numero = 2
        
    return numero


lista = []
lista_stt = []

dados_csv = csv.reader(open('BD_HORARIO_ATUAL.csv'), delimiter=';')
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
    print(integer(index[0]))
    

    id_course = Courses.objects.get(value=integer(index[0]))
   

    if id_course:
        query = Horario.objects.create(
        id_course_id=id_course.value,
        curso=id_course.name,
        periodo=index[1],
        disciplina=index[2],
        sala=index[3],
        dia=index[4],
        serie=index[5],
        professor=index[6]
        )
        print('index: {} Sucess! - Curso:{} | dia:{} '.format(i, index[0], index[4]))
  
    i+=1
# terminal$ python manage.py shell < app_vg/blo/shell_vg.py
# no projeto no terminal$ python manage.py shell < blo/shell_vg.py