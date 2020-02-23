from django.shortcuts import render
from .models import Preferences, Person, Game
import django_filters
from django.db import models
from django.views import View
from django.views import generic

class Persons_view(generic.ListView):
    model = Person





'''
def wybierz_gre(request):
    p_obj = Person.objects.get(id=1)
    kontekst = {
        'nazwa' : p_obj.name,
        'preferencja' : p_obj.preferences
    }
    return render(request, "index.html", kontekst)

class PersonFilter(django_filters.FilterSet):
    choosen = django_filters.BooleanFilter(name='choose', lookup_expr='isnull')

    class Meta:
        model = Person
        fields = ['choose']
        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                }
            }
        }
'''