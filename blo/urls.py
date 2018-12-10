from django.urls import path
from . import views
from .json_print import Json_Print
from .graphycs import *

urlpatterns = [
    path('', views.home, name='home'),
    path('json_print/', Json_Print.json_print),
    path('curso_json/', curso_json),
    path('post_graphs/', views.post_graphs, name='post_graphs'),
    path('curso_not_js/', curso_not_js),
    path('confirm_graphs/', views.confirm_graphs, name='confirm_graphs'),
    path('print_graphs/', views.print_graphs, name='print_graphs'),
    path('confirm_sala_js/', confirm_sala_js),
    path('print_js/', print_js),
    path('confirm_curM_js', confirm_curM_js),
    path('confirm_curN_js', confirm_curN_js),
]