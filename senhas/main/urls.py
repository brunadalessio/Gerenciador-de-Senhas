from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar, name='registrar'),
    path('painel/', views.painel, name='painel'),
    path('add/', views.add_senha, name='add_senha'),
    path('editar/<id>', views.edit_senha, name='editar_senha'),
    path('deletar/<id>', views.delete_senha, name='deletar_senha'),
]