from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def livro(request):
    return render(request, 'livro.html')

def sobre(request):
    return render(request, 'sobre.html')
