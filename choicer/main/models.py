from typing import List, Tuple
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

game_type_like_choices: List[Tuple[str, str]] = [
    ('', ''),
    ('Gra strategiczna', 'Gra strategiczna'),  # 2 slowo wyswietla to co widzi użytkownik
    ('Eurogry', 'Eurogry'),
    ('Ameritrashe', 'Ameritrashe'),
    ('Gry bitewne i wojenne', 'Gry bitewne i wojenne'),
    ('Gry kooperacyjne', 'Gry kooperacyjne'),
    ('Gry ekonomiczne', 'Gry ekonomiczne'),
    ('Gry imprezowe', 'Gry imprezowe'),
    ('Gry rodzinne', 'Gry rodzinne'),
]


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)
    game_type_like = models.CharField(
        verbose_name="Jaki typ gry lubi ta osoba najbardziej",
        max_length=30,
        choices=game_type_like_choices,
        default='wybierz',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person-detail", args=[self.pk])


class Game(models.Model):
    name = models.CharField(verbose_name="Nazwa gry", max_length=128, blank=True)
    image = models.ImageField(verbose_name="Zdjęcie gry", null=True, blank=True, upload_to="game_images")
    min_player = models.PositiveSmallIntegerField(verbose_name="Minimalna liczba graczy", blank=True, null=True)
    max_player = models.PositiveSmallIntegerField(verbose_name="Maksymalna liczb graczy", blank=True, null=True)
    game_type = models.CharField(
        verbose_name="Jaki to typ gry",
        max_length=30,
        choices=game_type_like_choices,
        default='',
        blank=True,
    )
    owner = models.ManyToManyField(Person)

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
