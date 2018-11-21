from django.shortcuts import render
from .models import *
from django.db.models import Q

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

    context = {'post':post}
    return render(request, 'blo/home.html', context)
