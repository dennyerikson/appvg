import csv
from blo.models import Courses

def integer(texto):
    lista = []
    numero = 0
    for i in range(2,100):
        lista.append("{}".format(i))
    print(texto)
    if texto in lista:
        inteiro = lista.index(texto)
        numero = int(lista[inteiro])
        
    return numero

lista = []
lista_stt = []

dados_csv = csv.reader(open('BD_COURSE.csv'), delimiter=';')
for [value, name] in dados_csv:
    lista.append('{};{}'.format(
        value, name)
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

    # try:
    query = Courses.objects.create(
    value=integer(index[0]),
    name=index[1],
    
    )
    print('Course: {} Sucess! - Curso:{} '.format(i, index[0], index[1]))
    # except:
    #     print('Course: {} Não cadastrado! - Curso:{} '.format(i, index[0], index[1]))
    i+=1
# terminal$ python manage.py shell < app_vg/blo/shell_courses.py
# no projeto no terminal$ python manage.py shell < blo/shell_courses.py