from django.urls import path
from .views import Game_view

urlpatterns = [
    path("", Game_view.as_view(), name='Game_view'),
]