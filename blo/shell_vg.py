import csv
from blo.models import Post

# vg_list = []

# with open('VG24.csv','r') as f:
#     r = csv.DictReader(f)

#     for [r_cpf] in r:
#         vg_list.append('{}'.format(r_cpf))
    
#     f.close()

# print(vg_list)



lista = []
lista_stt = []

dados_stt = csv.reader(open('VG24.csv'), delimiter=';')
for [stt_cpf, stt_nome, stt_sala] in dados_stt:
    lista.append('{};{};{}'.format(stt_cpf, stt_nome, stt_sala))
i=0
while i < len(lista):
    lista_stt.append(str(lista[i]).split(';'))
    i+=1


i=0
while i < len(lista_stt):
    index = lista_stt[i]
    index[0] = index[0]
    try:
        query = Post.objects.create(
        cpf=index[0],
        nome=index[1],
        sala=index[2]
        )
        print('index: {} Sucess! - {} '.format(i, index[0]))
    except:
        print('index: {} Não cadastrado! - {} '.format(i, index[0]))
    i+=1
#python manage.py shell < app_vg/blo/shell_vg.py