from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news.models import Articolo, Giornalista

# Create your views here.
""""
def home(request):
    return HttpResponse("<h1>Homepage news!</h1>")
"""

"""
AGGIUNGO GLI ELEMENTI DAL DATABASE
def home(request):
    a = ""
    g= ""
    for art in Articolo.objects.all():
        a += (art.articolo + "<br>")
    
    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli: <br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1>" + response + "</h1>")
"""

"""
USO DEGLI ARRAY
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    
    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
"""
def index(request):
    return render(request, "news/index.html")

def homepage(request):
    articoli= Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context= {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
    #articolo= Articolo.objects.get(pk=pk)
    articolo= get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)