import django_filters
from .models import Game


class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains') # to są specjalne warunki do pól
    min_player = django_filters.NumberFilter(lookup_expr='gte') # gte - great to equal
    max_player = django_filters.NumberFilter(lookup_expr='lte') # lte - less to equal
    class Meta:
        model = Game
        fields = ["game_type", "name", "min_player", "max_player", "owner"] # po tych polach mozna filtrować
