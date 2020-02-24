from django.shortcuts import render
from .models import Preferences, Person, Game
import django_filters
from django.db import models
from django.views import View
from django.views import generic

class Persons_view(generic.ListView):
    model = Person
    
# do testowania, widok, gdzie nie ma queryset
#  https://stackoverflow.com/questions/39012367/how-to-access-many-to-many-field-in-class-based-views-in-django
def person_view2(request, id)
    person = get_object_or_404(Person, id=id)
    pref_of_person = book.question.all()
    template = 'main/Person_list.html'
    ceontext = {'pref_of_person' : pref_of_person}
    return render(request, template, context)

#do testowania, ma zwracać liste gier gdzie pref sa takie same dla gry i osoby
#  https://stackoverflow.com/questions/7223463/django-select-object-from-db-in-a-template
game_list = []
for preferences in person.preferences:
    for preferences in game.preferences:
        try:
            best_option = Best_option.objects.get(preferences:preferences, preferences:preferences)
        except Best_option.DoesNotExist:
            best_optio = None
        game_list.append(best_option)
        
#  https://django-filter.readthedocs.io/en/master/ref/filters.html
#  filtry w django



'''
def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    authors_of_book = book.questions.all()
    template = 'books/book_detail1.html'
    context = {'authors_of_book': authors_of_book}
    return render(request, template, context)

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
