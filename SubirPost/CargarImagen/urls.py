from django.urls import path
from CargarImagen.views import show_posts
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', show_posts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)