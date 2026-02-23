from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto 
from forms_app.models import Contatto

def contatti(request):

    #se la richiesta è ti tipo POST allora possiamo processare i dati
    if request.method == "POST":

        form = FormContatto(request.POST)

        #is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            print("Il Form è valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])

            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
   
    #se la richiesta HTTp usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form= FormContatto()
    
    context = {"form": form}
    return render(request, "forms_app/contatto.html", context)

def index(request):
    return render(request, "forms_app/index.html")

def listaContatti(request):
    contatti = Contatto.objects.all()
    context = {'contatti': contatti}
    return render(request, "forms_app/lista_contatti.html", context)