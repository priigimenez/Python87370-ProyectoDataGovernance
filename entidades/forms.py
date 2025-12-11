from django import forms
from .models import Post, Category, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre de la categoría',
            'description': 'Descripción (ej: "Artículos sobre calidad de datos, gobierno de datos, etc.")'
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': 'Etiqueta (ej: "Data Quality", "Metadata", "Stewardship")'
        }

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Buscar posts', max_length=100, required=False)