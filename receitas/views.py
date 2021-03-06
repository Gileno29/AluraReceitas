from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render
from .models import Receita


# Create your views here.



def index(request):
    dados= {
        'receitas':Receita.objects.filter(publicada=True).order_by('data_receita')
    }
    return render(request,'index.html', dados)


def receitas(request, receita_id):
    receita= get_object_or_404(Receita, pk=receita_id)
   
    receita_a_exibir={
        'receita':receita
    }
    
    return render(request, 'receita.html', receita_a_exibir)

def testefiltro(request):
    receitas= {
        'receitas': Receita.objects.order_by('data_receita')
    }
    
    return  render(request,'teste_vfiltros.html',receitas)