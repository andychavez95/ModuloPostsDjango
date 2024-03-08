from django.shortcuts import render, redirect
from CargarImagen.forms import PostsForm
from CargarImagen.models import Posts


# Subida y validación de imagenes.
def show_posts(request):
    if request.method == 'POST':
        post_form = PostsForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect(show_posts)
    else :
        post_form = PostsForm()

    all_posts = Posts.objects.all()

    context = {
        'post_form': post_form,
        'posts': all_posts
    }

    return render(request, 'create_post.html', context)
