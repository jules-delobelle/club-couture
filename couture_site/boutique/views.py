from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cotisant, Produit, Achat
from .forms import AchatForm, UserRegisterForm
import unicodedata

import unicodedata

def clean_username(prenom, nom):
    username = (prenom + nom).lower().replace(' ', '')
    username = unicodedata.normalize('NFD', username).encode('ascii', 'ignore').decode("utf-8")
    return username



def acheter_produit(request):
    produits = Produit.objects.filter(stock__gt=0)
    if(request.method == "POST"):
        form = AchatForm(request.POST)
        if form.is_valid():
            produit = form.cleaned_data["produit"]
            quantite = form.cleaned_data["quantite"]
            cotisant = Cotisant.objects.first()
            prix_total = quantite * produit.prix
            if(produit.stock >= quantite and prix_total <= cotisant.solde):
                produit.stock -= quantite
                cotisant.solde -= prix_total
                produit.save()
                cotisant.save()
                achat = Achat(cotisant=cotisant, produit=produit, quantite=quantite)
                achat.save()
                messages.success(request, "Achat effectué avec succès.")
                return redirect("acheter")
    else:
        form = AchatForm()
    context = {
        "form": form,
        "produits": produits,
    }
    return render(request, "achat.html", context)


def inscription(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            username = clean_username(first_name, last_name)
            counter = 1
            original_username = username
            while User.objects.filter(username=username).exists():
                username = f"{original_username}{counter}"
                counter += 1

            user = form.save(commit=False)
            user.username = username
            user.save()
            cotisant = Cotisant(user=user, solde=20)
            cotisant.save()

            messages.success(request, "Votre compte a été créé avec succès.")
            login(request, user)
            return redirect("accueil")
    else:
        form = UserRegisterForm()
    return render(request, "inscription.html", {"form": form})


@login_required
def mon_compte(request):
    try:
        cotisant = request.user.cotisant
    except:
        messages.error(request, "Votre compte n'est pas encore activé, contactez le support")
        return redirect("accueil")
    achats = Achat.objects.filter(cotisant=cotisant)

    context = {
        "cotisant": cotisant,
        "achats": achats
    }

    return render(request, "mon_compte.html", context)

def accueil(request):
    return render(request, "accueil.html")


