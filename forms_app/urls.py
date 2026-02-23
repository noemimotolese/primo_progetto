from django.urls import path
from forms_app.views import index, contatti, listaContatti

app_name="forms_app"
urlpatterns=[
    #'' => pagina default
    path('index/', index, name='index'),
    path('contattaci/', contatti, name='contatti'),   
    path('lista_contatti/', listaContatti, name='lista_contatti'),   

]