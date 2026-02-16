from django.urls import path
from voti.views import view_a, index, view_b, view_c, view_d

app_name="voti"
urlpatterns=[
    #'' => pagina default
    path('index', index, name='index'),
    path('materie' , view_a, name='materie'),
    path('votiS' , view_b, name='votiS'),
    path('media' , view_c, name='media'),
    path('max_min' , view_d, name='max_min'),
]