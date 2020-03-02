from .models import Game
from django.forms import ModelForm


class GameTypeForm(ModelForm):
    class Meta:
        model = Game
        fields = ["game_type", "name", "min_player", "max_player"]
