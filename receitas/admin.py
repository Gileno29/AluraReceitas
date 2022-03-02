from django.contrib import admin
from .models import Receita
# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
    list_display= ('id','nome_receita')
    list_display_links=('id','nome_receita')

    


admin.site.register(Receita, ListandoReceitas)


