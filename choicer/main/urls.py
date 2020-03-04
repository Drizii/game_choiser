from django.urls import path
from .views import GameListView, GameDetailView, PersonDetailView

urlpatterns = [
    path("", GameListView.as_view(), name='Game_view'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'), # jezeli zmienie "game-detail" to wtedy absolute url nie generuje sie do linku
    path('user/<int:pk>', PersonDetailView.as_view(), name='person-detail'), # tu na końcu nie dajemy "/"
]
