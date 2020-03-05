from .models import Game, Person
from django.views.generic import ListView, DetailView
from .forms import GameTypeForm, RegisterForm
from django.views.generic import CreateView


class GameListView(ListView):
    model = Game
    template_name = "main/filtrujemy.html"
    context_object_name = 'game_list'
    ordering = "game_type"  # ordering = nazwa-pola // nazwa - to nazwa mojego pola, a pole to moje pole z modelu
    extra_context = {"form": GameTypeForm}

    def get_queryset(self):
        game_type = self.request.GET.get("game_type")
        name = self.request.GET.get("name")
        player_num = self.request.GET.get("player_num")
        owner = self.request.GET.get("owner")
        self.queryset = self.model.objects.all()
        if game_type:
            self.queryset = self.queryset.filter(game_type__icontains=game_type)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        if player_num:
            self.queryset = self.queryset.filter(min_player__lte=player_num, max_player__gte=player_num)  # TODO: zamina wyświetlanje nazwy
        if owner:
            self.queryset = self.queryset.filter(owner=owner)  # TODO: zamina wyświetlanje nazwy
        return super().get_queryset()
    # name__icontains wystarczy wpisać część słowa, aby zostały dopasowane wszystkie słowa np: mam w bazie name="bitewniak" i jak wpiszę "bi" to zadziała


class GameDetailView(DetailView):
    model = Game


class PersonDetailView(DetailView):
    model = Person
    context_object_name = "person_detail"


class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"


'''
def search(request):
    game_list = Game.object.all()
    game_filter = GameFilter(request.GET, queryset=game_list)
    return render(request, 'main/filtrujemy2_beta.html', {"filtr": game_filter})
'''