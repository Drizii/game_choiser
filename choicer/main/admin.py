from django.contrib import admin
from .models import Person, Game


admin.site.register(Person),
admin.site.register(Game),
# admin.site.register(UserGame # TODO: zastanwoić sie nad zaimplementowaniem tego