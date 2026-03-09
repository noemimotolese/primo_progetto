from django.shortcuts import render, redirect
from .forms import SignUpForm 
from django.contrib.auth import login

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST) #crea istanza con l'input dell'utente

        if form.is_valid(): #effettua la validazione
            user = form.save()
            login(request, user)
            return redirect('login') #eventualmente da personalizzare
        
    else: #richiesta di tipo get mostra il form vuoto
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
