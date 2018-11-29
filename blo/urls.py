from django.urls import path
from . import views
from .json_print import Json_Print

urlpatterns = [
    path('', views.home, name='home'),
    path('json_print/', Json_Print.json_print)
]