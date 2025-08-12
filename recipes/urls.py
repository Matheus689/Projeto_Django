# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# recipes/urls.py
from django.urls import path # Importa a função 'path' que define URLs.
from . import views # Importa o arquivo views.py do próprio app.

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'), # nova view para listar
]