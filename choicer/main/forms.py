from .models import Game, Person
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]