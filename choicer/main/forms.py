from .models import Game, Person
from django import forms


class GameTypeForm(forms.ModelForm):
    owner = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            required=False, queryset=Person.objects.all())

    class Meta:
        model = Game
        fields = "__all__"
