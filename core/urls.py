from django.urls import path
from .views import registro_usuario, HomeView, crear_proyecto, proyecto_detalle, lista_proyectos, alternar_tarea, eliminar_tarea, editar_proyecto, eliminar_proyecto
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('registro/', registro_usuario, name='registro'),
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #probar sin parametros
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    path('proyecto/nuevo/', crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:pk>/', proyecto_detalle, name='proyecto_detalle'),
    path('tarea/<int:pk>/alternar/', alternar_tarea, name='alternar_tarea'),
    path('tarea/<int:pk>/eliminar/', eliminar_tarea, name='eliminar_tarea'),
    path('proyecto/<int:pk>/editar/', editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', eliminar_proyecto, name='eliminar_proyecto'),
]

#as_view() transforma la clase HomeView en una función ejecutable para atender la petición HTTP.