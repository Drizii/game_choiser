from .models import Game, Person
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class GameTypeForm(forms.ModelForm):
    player_num = forms.IntegerField(
        label="Liczba graczy",
        min_value=1, max_value=99, required=False)
    owner = forms.ModelMultipleChoiceField(
            label="Właściciel",
            widget=forms.CheckboxSelectMultiple,
            required=False, queryset=Person.objects.all())  # to jest nowe pole, którego nie ma w models.py


    class Meta:
        model = Game
        exclude = ('image', 'min_player', 'max_player', 'description',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label="Nazwa użytkownika")
    password1 = forms.CharField(label="Hasło", help_text="Twoje hasło nie może być zbyt podobne do innych danych osobowych.<br>"
                                                         "Twoje hasło musi zawierać co najmniej 8 znaków.<br>"
                                                         "Twoje hasło nie może być powszechnie używanym hasłem.<br>"
                                                         "Twoje hasło nie może być całkowicie numeryczne.")

    password2 = forms.CharField(label="Powtórz hasło", help_text="W celu weryfikacji powtórz hasło.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
