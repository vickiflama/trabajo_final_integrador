from django.urls import path

from .views import  PerfilesListView ,\
                    PerfilesDetailView ,\
                    PerfilesUpdateView ,\
                    PerfilesDeleteView ,\
                    PerfilesCreateView

app_name = "perfiles"

urlpatterns = [
    path("", PerfilesListView.as_view(), name = "all"),
    path("<int:pk>/detail/", PerfilesDetailView.as_view(), name = "detail"),
    path("<int:pk>/update/", PerfilesUpdateView.as_view(), name = "update"),
    path("<int:pk>/delete/", PerfilesDeleteView.as_view(), name = "delete"),
    path("create/", PerfilesCreateView.as_view(), name = "create"),
]

# from django.contrib import admin
# from django.urls import path, include
# #Traer, importar cada def
# from Portfolio.views import * #si no va el nombre de cada vista
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls), #Nombre de la funcion del archivo views
#     path('', index, name = 'index'),   #Colocada como vista principal, HOME. En name indico el html al que va linkeado
#     path('nosotros', nosotros, name = 'nosotros'),
#     path('nosotreees', include('Perfiles.urls')),
#     path('registrarPerfil/', registrarPerfil),
#     path('eliminarP/<int:id>', eliminarP),
#     path('edicionP/<int:id>', edicionP),
#     path('editarP', editarP),
#     path('skills', skills, name = 'skills'),
#     path('contacto', contacto, name = 'contacto')
# ]
