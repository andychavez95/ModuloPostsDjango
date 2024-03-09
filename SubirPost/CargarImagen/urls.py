from django.urls import path
from CargarImagen.views import show_posts

urlpatterns = [
    path('', show_posts)
]