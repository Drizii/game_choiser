from django.urls import path, include
from .views import GameListView, GameDetailView, PersonDetailView, UserCreateView
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameList


urlpatterns = [
    path("", GameListView.as_view(), name='Game_view'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'), # jezeli zmienie "game-detail" to wtedy absolute url nie generuje sie do linku
    path('user/<int:pk>', PersonDetailView.as_view(), name='person-detail'), # tu na końcu nie dajemy "/"
    path('user/register', UserCreateView.as_view(), name="register"),
    path('user/', include("django.contrib.auth.urls")),
    #path("create/", views.create, name="create"), # TODO: zastanwoić sie nad zaimplementowaniem tego
    path("games/", views.GameList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)   # TODO: test serializer  - REST API
