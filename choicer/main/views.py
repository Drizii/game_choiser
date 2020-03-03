from .models import Game
from django.views. generic import ListView
from .forms import GameTypeForm
from .filter import GameFilter
from django.shortcuts import render


class GameListView(ListView):
    model = Game
    template_name = "main/filtrujemy.html"
    context_object_name = 'game'
    ordering = "game_type"  # ordering = nazwa-pola // nazwa - to nazwa mojego pola, a pole to moje pole z modelu
    extra_context = {"form": GameTypeForm}

    def get_queryset(self):
        game_type = self.request.GET.get("game_type")
        name = self.request.GET.get("name")
        min_player = self.request.GET.get("min_player")
        max_player = self.request.GET.get("max_player")
        if game_type:
            self.queryset = self.model.objects.filter(game_type__icontains=game_type)
        elif name:
            self.queryset = self.model.objects.filter(name__icontains=name)
        elif min_player:
            self.queryset = self.model.objects.filter(min_player__gte=min_player)
        elif max_player:
            self.queryset = self.model.objects.filter(max_player__lte=max_player)
        return super().get_queryset()
    # name__icontains wystarczy wpisać część słowa, aby zostały dopasowane wszystkie słowa np: mam w bazie name="bitewniak" i jak wpiszę "bi" to zadziała


def search(request):
    game_list = Game.object.all()
    game_filter = GameFilter(request.GET, queryset=game_list)
    return render(request, 'main/filtrujemy2_beta.html', {"filtr": game_filter})
