from django.urls import path

from . import views

app_name = 'sheet'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('<int:character_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('api/characters/<int:character_id>', views.getCharacter, name='getCharacter'),
]