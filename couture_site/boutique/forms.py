from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produit

class AchatForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.filter(stock__gt=0), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
        }


