from django.urls import path
from forms_app.views import index, contatti, listaContatti, modifica_contatto, elimina_contatto

app_name="forms_app"
urlpatterns=[
    #'' => pagina default
    path('index/', index, name='index'),
    path('contattaci/', contatti, name='contatti'),   
    path('lista_contatti/', listaContatti, name='lista_contatti'),   
    path('modifica-contatto/<int:pk>', modifica_contatto, name='modifica-contatto'),   
    path('elimina-contatto/<int:pk>', elimina_contatto, name='elimina-contatto'),   
]