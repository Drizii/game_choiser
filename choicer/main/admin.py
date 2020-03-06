from django.contrib import admin
from .models import Person, Game, GameType, MechanicType


admin.site.register(Person),
admin.site.register(Game),
admin.site.register(GameType),
admin.site.register(MechanicType),