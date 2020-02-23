from django.db import models


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
