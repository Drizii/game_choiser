from .models import Game, Person
from django import forms


class GameTypeForm(forms.ModelForm):
    player_num = forms.IntegerField(
        min_value=1, max_value=99, required=False
    )
    owner = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            required=False, queryset=Person.objects.all())


    class Meta:
        model = Game
        exclude = ('image', 'min_player', 'max_player')
