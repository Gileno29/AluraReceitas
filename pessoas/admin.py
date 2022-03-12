from django.contrib import admin
from .models import Pessoa

# Register your models here.
class ListandoPessoas(admin.ModelAdmin):
     list_display= ('nome','email')
admin.site.register(Pessoa, ListandoPessoas)
