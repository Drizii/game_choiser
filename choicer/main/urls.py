from django.urls import path
from .views import GameListView, GameDetailView
from django_filters.views import FilterView
from .filter import GameFilter

urlpatterns = [
    path("", GameListView.as_view(), name='Game_view'),
    path("a", FilterView.as_view(filterset_class=GameFilter, template_name='main/filtrujemy2_beta.html'), name='search'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]
