from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.csrf import csrf_failure
from .models import Cotisant, Produit, Achat
from .forms import AchatForm, UserRegisterForm

# Create your views here.

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
                return redirect("achat")
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
            user = form.save()
            cotisant = Cotisant(user=user, solde = 20)
            cotisant.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            login(request, user)
            return redirect("accueil")
    else:
        form = UserRegisterForm()
    return render(request, "inscription.html", {"form": form})


