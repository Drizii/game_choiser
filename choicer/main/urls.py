from django.urls import path, include
from .views import GameListView, GameDetailView, PersonDetailView, UserCreateView
from django.views.generic import TemplateView


urlpatterns = [
    path("", GameListView.as_view(), name='Game_view'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),  # jezeli zmienie "game-detail" to wtedy absolute url nie generuje sie do linku
    path('user/<int:pk>', PersonDetailView.as_view(), name='person-detail'),  # tu na końcu nie dajemy "/"
    path('user/register', UserCreateView.as_view(), name="register"),
    path('user/logout', TemplateView.as_view(template_name="logout.html")),
    path('user/', include("django.contrib.auth.urls")),
]
