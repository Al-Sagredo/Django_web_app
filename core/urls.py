from django.urls import path
from .views import registro_usuario, HomeView

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('', HomeView.as_view(), name='home')
]

#as_view() transforma la clase HomeView en una función ejecutable para atender la petición HTTP.