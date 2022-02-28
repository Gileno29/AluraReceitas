from django.shortcuts import render
from .models import Receita


# Create your views here.



def index(request):
    dados= {
        'receitas':Receita.objects.all()
    }
    return render(request,'index.html', dados)

def receitas(request):
    return render(request, 'receita.html')