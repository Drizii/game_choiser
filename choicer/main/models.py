from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User
# TODO: zrobić podział w admnieni na kategorie klas


class GameType(models.Model):
    name = models.CharField(verbose_name="Nazwa kategotii", max_length=128, blank=True, null=True)
    description = models.TextField(verbose_name="Opis kategorii", max_length=1126, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Typ gry"  # pozwala podać nazwe pola w liczbie pojedynczej
        verbose_name_plural = "_Typy Gry"  # pozwala zmienić nazwe pola na liście modeli w Adminie


class MechanicType(models.Model):
    name = models.CharField(verbose_name="Nazwa mechaniki", max_length=128, blank=True, null=True)
    description = models.TextField(verbose_name="Opis mechaniki", max_length=1126, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mechanika"
        verbose_name_plural = "_Mechaniki gier"


class Users(User):
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse("person-detail", args=[self.pk])


class Game(models.Model):
    name = models.CharField(verbose_name="Nazwa gry", max_length=128, blank=True)
    description = models.TextField(verbose_name="Opis gry", blank=True)
    image = models.ImageField(verbose_name="Zdjęcie gry", null=True, blank=True, upload_to="game_images")
    min_player = models.PositiveSmallIntegerField(verbose_name="Minimalna liczba graczy", blank=True, null=True)
    max_player = models.PositiveSmallIntegerField(verbose_name="Maksymalna liczb graczy", blank=True, null=True)
    min_play_time = models.PositiveIntegerField(verbose_name="Minimalny czas gry(minuty)", blank=True, null=True)
    game_type = models.ManyToManyField(GameType, verbose_name="Rodzaj gry", blank=True)  # TODO: mozna zaimplementowac checkboxy do zaznaczania w adminie
    mechanic_type = models.ManyToManyField(MechanicType, verbose_name="Rodzaj gry", blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        self.clean_players()
        super().clean()  # super pozwala zachować dane, które normalnie zostalby nadpisane, tu zamiast @clean były próby używania save i __init__ ale nie działało :/, save dawalo komunika na stronie z błędem a __init__ nie działało  wcale, mozna pokombinowac aby błąd pojawiał sie w innym miejscu, ale narazie tyle starczy

    def clean_players(self):
        if self.max_player - self.min_player < 0:
            raise ValidationError("Maksymalna liczba graczy musi być większa niż minimalna")

    def get_absolute_url(self):
        return reverse("game-detail", args=[self.pk])

    def __str__(self):
        return self.name

# https://rk.edu.pl/pl/widok-filtrujcy-w-django/
