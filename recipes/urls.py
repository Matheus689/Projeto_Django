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
# recipes/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    # Esta linha é crucial: define a URL e nomeia ela como 'recipe_detail'
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    # Outras URLs do seu aplicativo...
]