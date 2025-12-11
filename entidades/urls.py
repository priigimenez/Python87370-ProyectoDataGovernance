from django.urls import path
from .views import home, posts, create_category, create_tag, search_posts, about, post_detail

urlpatterns = [
    path('', home, name='home'),
    path("posts/", posts, name="posts"),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path("buscar/", search_posts, name="search_posts")
    ,path("categorias/nueva/", create_category, name="create_category")
    ,path("etiquetas/nueva/", create_tag, name="create_tag")
    ,path("sobre-mi/", about, name="about")
]