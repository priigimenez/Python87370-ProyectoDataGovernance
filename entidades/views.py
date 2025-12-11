from django.shortcuts import get_object_or_404
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'entidades/post_detail.html', {'post': post})
def about(request):
    return render(request, 'entidades/about.html')
from django.db.models import Q
def search_posts(request):
    from .forms import PostSearchForm
    form = PostSearchForm(request.GET or None)
    results = []
    if form.is_valid() and form.cleaned_data['query']:
        q = form.cleaned_data['query']
        results = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'entidades/search_posts.html', {'form': form, 'results': results})
from django.shortcuts import render

from .models import Post
from .forms import PostForm, CategoryForm, TagForm

# Create your views here.

def home(request):
    ultimo_post = Post.objects.order_by('-created_at').first()
    return render(request, 'entidades/index.html', {'ultimo_post': ultimo_post})

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