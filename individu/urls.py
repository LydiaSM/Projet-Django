from django.urls import path
from . import views
urlpatterns = [
    path('', views.accueil, name='accueil'),

    path('groupe/', views.groupe_list, name='groupe_list'),
    path('groupe/nv/', views.NVgroupe, name='NVgroupe'),
    path('groupe/<int:pk>/', views.groupe_detail, name='groupe_detail'),


    path('individu/', views.individu_list, name='individu_list'),
    path('individu/nv/', views.NVindividu, name='NVindividu'),
    path('individu/<int:pk>/', views.Detail, name='Detail'),
    path('indivu/<int:pk>/modifier/', views.ModifIndividu, name='ModifIndividu'),
]