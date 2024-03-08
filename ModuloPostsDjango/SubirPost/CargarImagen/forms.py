from django import forms
# from models import Posts
from CargarImagen.models import Posts

# Formulario para Posts.
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['image', 'comment']