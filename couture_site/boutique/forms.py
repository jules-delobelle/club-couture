from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produit

class AchatForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.filter(stock__gt=0), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")

class UserRegisterForm(UserCreationForm):
    prenom = forms.CharField(max_length=100, label="Prénom")
    nom = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="Email")
    mdp = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    mdp2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


