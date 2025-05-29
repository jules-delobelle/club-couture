from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import acheter_produit, inscription, mon_compte, accueil


urlpatterns = [
    path("acheter/", acheter_produit, name="acheter"),
    path("inscription/", inscription, name="inscription"),
    path("connexion/", LoginView.as_view(template_name="connexion.html"), name="connexion"),
    path("deconnexion/", LogoutView.as_view(next_page="connexion"), name="deconnexion"),
    path("mon_compte/", mon_compte, name="mon_compte"),
    path("accueil/", accueil, name="acceuil")
]
