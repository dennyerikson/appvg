import csv
from blo.models import Post, Horario

# vg_list = []

# with open('VG24.csv','r') as f:
#     r = csv.DictReader(f)

#     for [r_cpf] in r:
#         vg_list.append('{}'.format(r_cpf))
    
#     f.close()

# print(vg_list)



lista = []
lista_stt = []

dados_csv = csv.reader(open('BD_HORARIO.csv'), delimiter=';')
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
    index = lista_stt[i]
    index[0] = index[0]
    try:
        query = Horario.objects.create(
        curso=index[0],
        periodo=index[1],
        disciplina=index[2],
        sala=index[3],
        dia=index[4],
        serie=index[5],
        professor=index[6]
        )
        print('index: {} Sucess! - {} '.format(i, index[0]))
    except:
        print('index: {} Não cadastrado! - {} '.format(i, index[0]))
    i+=1
# terminal$ python manage.py shell < app_vg/blo/shell_vg.py
# no projeto no terminal$ python manage.py shell < blo/shell_vg.py