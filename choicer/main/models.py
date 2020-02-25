from django.db import models
from django.core.exceptions import ValidationError


class Preferences(models.Model):
    pref = models.CharField(max_length=64)

    def __str__(self):
        return self.pref


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)
    game_type_like = models.PositiveIntegerField(default=12)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(verbose_name="Nazwa gry", max_length=128)
    min_player = models.PositiveSmallIntegerField(verbose_name="Minimalna liczba graczy", default=0)
    max_player = models.PositiveSmallIntegerField(verbose_name="Maksymalna liczb graczy", default=0)


    class Game(models.Model):
        def clean(self, *args, **kwargs):
            self.clean_players()
            return super().clean(*args, **kwargs)  # super pozwala zachować dane, które normalnie zostalby nadpisane

        def clean_players():
            if self.max_players - self.min_players < 0:
                raise ValidationError("Maksymalna liczba graczy msui być więskza niż minimalna")

    def __str__(self):
        return self.name

'''   Marcinkowa funkcja majaca sprawdzic ilosc graczy - ale nie dziala
    class Game(models.Model):
        def __init__(self, *args, **kwargs):
            self.clean_players()
            super().__init__(*args, **kwargs) # super pozwala zachować dane, które normalnie zostalby nadpisane
            

        def clean_players():
            if self.max_players - self.min_players < 0:
                raise ValidationError("Maksymalna liczba graczy msui być więskza niż minimalna")

class Preferences(models.Model):
    pref = models.CharField(max_length=64)

    def __str__(self):
        return self.pref


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)
    preferences = models.ManyToManyField(Preferences, verbose_name="Preferencja gracza")
    choose = models.BooleanField(verbose_name="Wybierz",  blank=False, default=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(verbose_name="Nazwa gry", max_length=128)
    preferences = models.ManyToManyField(Preferences, verbose_name="Preferencja gracza")

    def __str__(self):
        return self.name
'''