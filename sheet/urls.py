from django.urls import path
from . import views

app_name = "sheet"

urlpatterns = [
    path("", views.listCharacters, name="index"),
    path("create", views.create, name="create"),
    path("api/characters", views.listCharacters, name="listCharacters"),
    path("api/characters/<int:characterId>", views.getCharacter, name="getCharacter"),
    path(
        "api/characters/<int:characterId>/level",
        views.getCharacterWithLevel,
        name="getCharacterWithLevel",
    ),
    path("api/characters/<int:characterId>/plan", views.getPlan, name="getPlan"),
]
