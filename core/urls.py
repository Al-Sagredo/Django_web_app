from django.urls import path
from .views import registro_usuario, HomeView
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('registro/', registro_usuario, name='registro'),
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #probar sin parametros
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

#as_view() transforma la clase HomeView en una función ejecutable para atender la petición HTTP.