from django.urls import path
from . import views
urlpatterns = [
    path('', views.individu_list, name='individu_list'),
    path('individu/<int:pk>/', views.Action, name='Action'),
]