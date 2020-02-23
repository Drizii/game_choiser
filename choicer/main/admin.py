from django.contrib import admin
from .models import Preferences, Person, Game


admin.site.register(Person),
admin.site.register(Preferences),
admin.site.register(Game),