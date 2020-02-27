from .models import Game, Person
from django.views. generic import ListView


class GameListView(ListView):
    model = Game
    template_name = "main/filtrujemy.html"
    context_object_name = 'game'
    ordering = "game_type"  #ordering = nazwa-pola // nazwa - to nazwa mojego pola, a pole to moje mole z modelu

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            self.queryset = self.model.objects.filter(name__icontains=name)
            # name__icontains wystarczy wpisać część słowa, aby zostały dopasowane wszystkie słowa np: mam w bazie name="bitewniak" i jak wpiszę "bi" to zadziała
        return super().get_queryset()

    def get_queryset(self):
        game_type = self.request.GET.get("game_type")
        if game_type:
            self.queryset = self.model.objects.filter(game_type__icontains=game_type)
        return super().get_queryset()

























'''
class PersonListView(ListView):
    model = Person
    template_name = 'main/PersonTest'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonFilter(self.request.GET, queryset=self.get_queryset())
        return context










def annotate_m2m(queryset, fields, main_model, joined_model, rel_field, promote=False):

    parametry:
            queryset - queryset na którym dokonujemy operacji
            fields - słownik pól w formacie {'nazwa_atrybutu_dodanego': 'pole_w_formacie_sql_tabela.pole'}
            main_model - klasa modelu, z którego rozpoczynamy join
            joined_model - klasa modelu, na którym kończymy join
            rel_field - pole relacji w pierwszym modelu
            promote - ustawione na False joinuje przy pomocy INNER JOIN,
                      ustawione na True joinuje przy pomocy LEFT OUTER JOIN

    zwraca:
        queryset z dodanymi polami ze słownika fields


    # dodajemy wymagane pola do querysetu
    queryset = queryset.extra(select=fields)

    # pobieramy pole relacji
    related_field = getattr(main_model, rel_field)

    # inicjalizujemy JOIN
    queryset.query.join((None, main_model._meta.db_table, None, None))

    # tworzymy odpowiednie reguły joinów wg schematu:
    # (tabela dołączająca, tabela dołączana, pole relacji tabeli pierwszej, pole relacji tabeli drugiej)
    connection_m2m = (
        main_model._meta.db_table,  # tabela dołączająca
        related_field.field.m2m_db_table(),  # tabela łącząca
        main_model._meta.pk.column,  # pole relacji z pierwszej tabeli
        related_field.field.m2m_column_name(),  # pole relacji z drugiej tabeli
    )

    connection_dest = (
        related_field.field.m2m_db_table(),  # tabela łącząca
        joined_model._meta.db_table,  # tabela dołączana
        related_field.field.m2m_reverse_name(),  # pole relacji z pierwszej tabeli
        joined_model._meta.pk.column,  # pole realcji z drugiej tabeli
    )

    # dołączenia
    queryset.query.join(connection_m2m, promote=promote)
    queryset.query.join(connection_dest, promote=promote)

    return queryset





# https://programowo.net/2014/05/reczny-join-w-django-do-tabel-many-to-many,113.html
    
def annotate_m2m(queryset, fields, main_model, joined_model, rel_field, promote=False):

    parametry:
            queryset - queryset na którym dokonujemy operacji
            fields - słownik pól w formacie {'nazwa_atrybutu_dodanego': 'pole_w_formacie_sql_tabela.pole'}
            main_model - klasa modelu, z którego rozpoczynamy join
            joined_model - klasa modelu, na którym kończymy join
            rel_field - pole relacji w pierwszym modelu
            promote - ustawione na False joinuje przy pomocy INNER JOIN,
                      ustawione na True joinuje przy pomocy LEFT OUTER JOIN

    zwraca:
        queryset z dodanymi polami ze słownika fields
    

    # dodajemy wymagane pola do querysetu
    queryset = queryset.extra(select=fields)

    # pobieramy pole relacji
    related_field = getattr(main_model, rel_field)

    # inicjalizujemy JOIN 
    queryset.query.join((None, main_model._meta.db_table, None, None))

    # tworzymy odpowiednie reguły joinów wg schematu:
    # (tabela dołączająca, tabela dołączana, pole relacji tabeli pierwszej, pole relacji tabeli drugiej)
    connection_m2m = (
        main_model._meta.db_table,  # tabela dołączająca
        related_field.field.m2m_db_table(),  # tabela łącząca
        main_model._meta.pk.column,  # pole relacji z pierwszej tabeli
        related_field.field.m2m_column_name(),  # pole relacji z drugiej tabeli
    )

    connection_dest = (
        related_field.field.m2m_db_table(),  # tabela łącząca
        joined_model._meta.db_table,  # tabela dołączana
        related_field.field.m2m_reverse_name(),  # pole relacji z pierwszej tabeli
        joined_model._meta.pk.column,  # pole realcji z drugiej tabeli
    )

    # dołączenia
    queryset.query.join(connection_m2m, promote=promote)
    queryset.query.join(connection_dest, promote=promote)

    return queryset
    
    
    
class Persons_view(generic.ListView):
    model = Person


#do testowania, ma zwracać liste gier gdzie pref sa takie same dla gry i osoby
#  https://stackoverflow.com/questions/7223463/django-select-object-from-db-in-a-template
game_list = []
for preferences in person_list:
    for preferences in game_list:
        try:
            best_option = Best_option.objects.get(preferences : preferences)
        except Best_option.DoesNotExist:
            best_option = None
        game_list.append(best_option)


# do testowania, widok, gdzie nie ma queryset
#  https://stackoverflow.com/questions/39012367/how-to-access-many-to-many-field-in-class-based-views-in-django
def person_view2(request, id):
    person = get_object_or_404(Person, id=id)
    pref_of_person = person.question.all()
    template = 'main/Person_list.html'
    context = {'pref_of_person' : pref_of_person}
    return render(request, template, context)
    
        
#  https://django-filter.readthedocs.io/en/master/ref/filters.html
#  filtry w django

#  https://stackoverflow.com/questions/45670381/how-to-display-records-belongs-to-categories-in-django
#  ciekawa apka - sprawdzic




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
