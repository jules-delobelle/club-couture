from django import forms
from .models import Produit

class AchatForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.filter(stock__gt=0), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")