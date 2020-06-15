from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:movie_id>/', views.detail, name='detail'),
    path('<str:movie_id>/watched/', views.watched, name='watched')
]