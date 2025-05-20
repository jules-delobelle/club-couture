from django.db import models

# Create your models here.

class Cotisant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    solde = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nom.upper} {self.prenom.capitalize} ({self.solde})"
    
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nom} ({self.stock} en stock)"
    
class Achat(models.Model):
    cotisant = models.ForeignKey(Cotisant, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cotisant} a acheté {self.quantite} x {self.produit.nom}"