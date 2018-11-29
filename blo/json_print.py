from django.db.models import Count
from django.http import JsonResponse
from .models import Post
import json

cpf = ''
sala = ''

class Json_Get(object):
    cpf = ' '
    sala = ' '

class Json_Print(object):

    def json_print(request):
        lista ='{"cpf":'+Json_Get.cpf+', "sala":'+Json_Get.sala+'}'

        return JsonResponse({'print':lista})

    def post_serializer(item): #serealiza para dicionário
        return {'cpf':item['cpf'], 'quantidade': item['value']}
