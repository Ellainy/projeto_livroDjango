from django.shortcuts import render
from .models import HomePage, Livro, Sobre, Pagina

def home(request):
    home_page = HomePage.objects.first() 
    return render(request, 'index.html', {'home_page': home_page})

def livro(request):
    livro = Livro.objects.first()
    #paginas = livro.paginas.all()  
    return render(request, 'livro.html', {'livro': livro})

def sobre(request):
    sobre_info = Sobre.objects.first()  
    return render(request, 'sobre.html', {'sobre': sobre_info})

def lerlivro(request):
    return render(request, 'lerlivro.html')

def login(request):
    return render(request, 'login.html')
