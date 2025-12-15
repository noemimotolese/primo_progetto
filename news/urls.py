from django.urls import path
from .views import homepage, articoloDetailView, index

app_name = 'news'

urlpatterns = [
    path('', index, name= "index"),
    path('homepage', homepage, name = "homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]
