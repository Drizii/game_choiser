from .views import Persons_view
from django.urls import path
app_name = 'main'

urlpatterns = [
    path('', view=Persons_view.as_view(), name='Persons_view'),
]