from django.urls import path
from . import views
urlpatterns = [
    path('', views.individu_list, name='individu_list'),
    path('individu/<int:pk>/', views.Detail, name='Detail'),
    path('individu/nv/', views.NVindividu, name='NVindividu'),
    path('indivu/<int:pk>/modifier/', views.ModifIndividu, name='ModifIndividu'),
]