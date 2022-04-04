from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receitas, name='receita'),
    path('teste_filtros', views.testefiltro, name='teste_filtros')
]