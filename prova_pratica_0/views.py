from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "prova_pratica_0/index.html")

def view_a(request):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    somma = num1 + num2
    context = {
        "num1": num1,
        "num2" : num2,
        "somma" : somma
    }
    return render(request, "view_a.html", context)

def view_b(request):
    lista = []
    somma = 0
    
    for i in range(30):
        lista.append(random.randint(1, 10))

    for n in lista:
        somma += n 

    media = somma/len(lista)

    context = {
        "listaNum" : lista,
        "sommaN" : somma,
        "mediaN" : media
    }
    return render(request, "view_b.html", context)
