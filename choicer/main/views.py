from .models import Game, Person
from django.views.generic import ListView, DetailView
from .forms import GameTypeForm
from django.shortcuts import get_object_or_404, render


class GameListView(ListView):
    model = Game
    template_name = "main/filtrujemy.html"
    context_object_name = 'game_list'
    ordering = "game_type"  # ordering = nazwa-pola // nazwa - to nazwa mojego pola, a pole to moje pole z modelu
    extra_context = {"form": GameTypeForm}

    def get_queryset(self):
        game_type = self.request.GET.get("game_type")
        name = self.request.GET.get("name")
        min_player = self.request.GET.get("min_player")
        max_player = self.request.GET.get("max_player")
        owner = self.request.GET.get("owner")
        self.queryset = self.model.objects.all()
        if game_type:
            self.queryset = self.queryset.filter(game_type__icontains=game_type)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        if min_player:
            self.queryset = self.queryset.filter(min_player__gte=min_player)
        if max_player:
            self.queryset = self.queryset.filter(max_player__lte=max_player)
        if owner:
            self.queryset = self.queryset.filter(owner__icontains=owner)
        return super().get_queryset()
    # name__icontains wystarczy wpisać część słowa, aby zostały dopasowane wszystkie słowa np: mam w bazie name="bitewniak" i jak wpiszę "bi" to zadziała


class GameDetailView(DetailView):
    model = Game


class PersonListView(ListView): # wylistowanie gier, które są posiadane przez właściciela
    model = Person

class PersonDetailView(DetailView):
    model = Person

'''
def search(request):
    game_list = Game.object.all()
    game_filter = GameFilter(request.GET, queryset=game_list)
    return render(request, 'main/filtrujemy2_beta.html', {"filtr": game_filter})
'''