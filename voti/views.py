from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "voti/index.html")

def get_voti():
    return {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context = {"materie": materie}
    return render(request, "voti/materie.html", context)

def view_b(request):
    voti = get_voti()
    context = {"voti": voti}
    return render(request, "voti/votiS.html", context)

def view_c(request):
    voti = get_voti()
    medie = {}
    for nome_studente, lista_voti in voti.items():
        somma = 0
        conta = 0
        for materia in lista_voti:
            somma += materia[1]
            conta += 1
        media = round((somma/conta),2)
        medie[nome_studente] = media

    context = {"medie": medie}

    return render(request, "voti/media.html", context)

def view_d(request):
    voti = get_voti()
    max=0
    min=100

    materiaMin = []
    materiaMax = []

    nomeMin = []
    nomeMax = []
    
    for nome_studente, lista_voti in voti.items():
        for materia in lista_voti:
            if materia[1] < min:
                min = materia[1]
            elif materia[1] > max:
                max = materia[1]

    for nome_studente, lista_voti in voti.items():
        for materia in lista_voti:
            if materia[1] == min:
                materiaMin.append(materia[0])
                nomeMin.append(nome_studente) 
            elif materia[1] == max:
                materiaMax.append(materia[0])
                nomeMax.append(nome_studente) 

    context = { "min": min,
                "max": max,
                "materiaMin": materiaMin,
                "materiaMax": materiaMax,
                "nomeMin": nomeMin,
                "nomeMax": nomeMax
              }
    
    return render(request, "voti/max_min.html", context)



            