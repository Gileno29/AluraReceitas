from re import search
from django.contrib import admin
from .models import Pessoa

# Register your models here.
class ListandoPessoas(admin.ModelAdmin):
     list_display= ('id','nome','email')
     search_fields=('nome',)
     list_filter=('nome',)
admin.site.register(Pessoa, ListandoPessoas)
