from django.shortcuts import render


# Create your views here.



def index(request):


    receitas={
        1:'lazanha',
        2:'cuzcuz',
        3:'salsicha ao molho',
        4:'salmão'

    }
    dados= {
        'nomes_das_receitas':receitas
    }
    return render(request,'index.html', dados)

def receitas(request):
    return render(request, 'receita.html')