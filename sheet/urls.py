from django.urls import path
from . import views

app_name = "sheet"

urlpatterns = [
    path("api/create", views.getCreationOptions, name="getCreationOptions"),
    path("api/characters", views.listCharacters, name="listCharacters"),
    path("api/characters/<int:characterId>", views.getCharacter, name="getCharacter"),
    path("api/characters/<int:characterId>/plan", views.getPlan, name="getPlan"),
    path(
        "api/characters/toggles/<int:characterId>",
        views.getCharacterWithToggles,
        name="getCharacterWithToggles",
    ),
]
