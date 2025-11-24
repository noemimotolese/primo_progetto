from django.urls import path
from prova_pratica_0.views import view_a, view_b, index

app_name="prova_pratica_0"
urlpatterns=[
    #'' => pagina default
    path('index', index, name='index'),
    path('view_a' , view_a, name='view_a'),
    path('view_b', view_b, name='view_b'),
]