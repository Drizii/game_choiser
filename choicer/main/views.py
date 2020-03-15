from .models import Game, Users
from django.views.generic import ListView, DetailView
from .forms import GameTypeForm, RegisterForm
from django.views.generic import CreateView


class GameListView(ListView):
    model = Game
    template_name = "main/filtrujemy.html"
    context_object_name = 'game_list'
    ordering = "name"  # ordering = nazwa-pola // nazwa - to nazwa mojego pola, a pole to moje pole z modelu
    extra_context = {"form": GameTypeForm}
    paginate_by = 5

    def get_queryset(self):  # TODO: Sorotwanie kolumn od najwiekszej do najmniejszej wartosci, do tego najlepiej JS
        game_type = dict(self.request.GET).get("game_type")
        name = self.request.GET.get("name")
        player_num = self.request.GET.get("player_num")
        min_play_time = self.request.GET.get("min_play_time")
        mechanic_type = dict(self.request.GET).get("mechanic_type")
        user = self.request.GET.get("user")
        self.queryset = self.model.objects.all()
        if game_type:
            self.queryset = self.queryset.filter(game_type__in=game_type)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        if player_num:
            self.queryset = self.queryset.filter(min_player__lte=player_num, max_player__gte=player_num)
        if min_play_time:
            self.queryset = self.queryset.filter(min_play_time__gte=min_play_time)
        if mechanic_type:
            self.queryset = self.queryset.filter(mechanic_type__in=mechanic_type)
        if user:
            self.queryset = self.queryset.filter(user=user)
        return super().get_queryset().distinct()  # TODO naprawić wyszukiwanie tak, aby byla mozliwosc wyszukania gier po polach game_type
    # name__icontains wystarczy wpisać część słowa, aby zostały dopasowane wszystkie słowa np: mam w bazie name="bitewniak" i jak wpiszę "bi" to zadziała


class GameDetailView(DetailView):
    model = Game


class PersonDetailView(DetailView):  # to zmienic na User'a TODO wyswietlanie jako profilu użytkownika, użytkownik moze dodać gry jako swoje
    model = Users
    template_name = "main/person_detail.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["games"] = self.object.game_set.all()
        return context_data


class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"


# TODO: zastanwoić sie nad zaimplementowaniem tego
# https://techwithtim.net/tutorials/django/user-specific-pages-data/
''' 
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = UserGames(name=n)
            t.save()
            response.user.usergame.add(t)  # adds the to do list to the current logged in user

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "test/create.html", {"form": form})

'''
'''
to jest do filtrujemy.py
def search(request):
    game_list = Game.object.all()
    game_filter = GameFilter(request.GET, queryset=game_list)
    return render(request, 'main/filtrujemy2_beta.html', {"filtr": game_filter})
'''