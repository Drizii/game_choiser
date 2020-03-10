from django.contrib import admin
from .models import Game, GameType, MechanicType, Users


admin.site.register(Game),
admin.site.register(GameType),
admin.site.register(MechanicType),
admin.site.register(Users),