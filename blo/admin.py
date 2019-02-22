from django.contrib import admin
from .models import *
# from .actions import SetarAdministracao, SetarEdfisica

class HorarioAdmin(admin.ModelAdmin):
    FIELDS =[
       'curso', 'disciplina', 'dia'
    ]
    list_filter = FIELDS
    search_fields = FIELDS
    list_display = FIELDS
    # actions = [ SetarAdministracao, SetarEdfisica]

class CoursesAdmin(admin.ModelAdmin):
    FIELDS = [
        'id', 'name', 'value'
    ]
    search_fields = FIELDS
    list_display = FIELDS

# Register your models here.
# admin.site.register(Post)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Courses, CoursesAdmin)
