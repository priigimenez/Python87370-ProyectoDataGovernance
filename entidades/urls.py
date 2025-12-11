from django.urls import path
from .views import home, posts, create_category, create_tag

urlpatterns = [
    path('', home, name='home'),
    path("posts/", posts, name="posts")
    ,path("categorias/nueva/", create_category, name="create_category")
    ,path("etiquetas/nueva/", create_tag, name="create_tag")
]