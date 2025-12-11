from django.shortcuts import render

from .models import Post
from .forms import PostForm, CategoryForm, TagForm

# Create your views here.

def home(request):
    return render(request, 'entidades/index.html')

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'entidades/create_category.html', {'form': form})

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            form = TagForm()
    else:
        form = TagForm()
    return render(request, 'entidades/create_tag.html', {'form': form})

def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user if request.user.is_authenticated else None
            post.save()
            form.save_m2m()
            form = PostForm()  # Limpiar el formulario tras guardar
    else:
        form = PostForm()
    contexto = {
        "Posts": Post.objects.all().order_by('-created_at'),
        "form": form
    }
    return render(request, 'entidades/posts.html', contexto)