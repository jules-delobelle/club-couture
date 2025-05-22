from django.urls import path
from .views import acheter_produit, inscription, LoginView, LogoutView

urlpatterns = [
    path('acheter/', acheter_produit, name='acheter'),
    path("inscription/", inscription, name="inscription"),
    path("connexion/", LoginView.as_view(template_name="connexion.html"), name="connexion"),
    path("deconnexion/", LogoutView.as_view(next_page="connexion"), name="deconnexion"),
]
