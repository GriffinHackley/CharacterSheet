from django.urls import path

from . import views

app_name = 'sheet'

urlpatterns = [
    # ex: /sheet/
    path('', views.index, name='index'),
    # ex: /sheet/5/
    path('<int:character_id>/', views.detail, name='detail'),
    path('delete/<int:character_id>/', views.delete, name='delete'),
    path('create', views.create, name='delete'),
]