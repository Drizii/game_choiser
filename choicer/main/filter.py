import django_filters
from .models import Game


class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Nazwa gry")  # to są specjalne warunki do pól
    min_player = django_filters.NumberFilter(lookup_expr='gte', label="Minimalna liczba graczy")  # gte - great to equal
    max_player = django_filters.NumberFilter(lookup_expr='lte', label="Maksymalna liczba graczy")  # lte - less to equal #label - za pomocą tego można podstawić dowolną nazwe ktora bedzie sie wyswietlala użytkownikowi

    class Meta:
        model = Game
        fields = ["game_type", "name", "min_player", "max_player", "owner"]  # po tych polach mozna filtrować
