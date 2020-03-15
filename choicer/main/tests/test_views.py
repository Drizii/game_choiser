from django.test import TestCase, Client
from django.urls import reverse

from main.tests.factories import GameFactory, GameTypeFactory


class GameListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("Game_view")  # revers tworzy scierze do url, url moge se zmieniac a testy maja to w dupie xd

    def tearDown(self):
        pass

    def test_return_200_when_view_is_called(self):
        # daj mi 200 jeśli pokazesz strone
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_return_games_with_filter_game_name(self):
        # test filtra "name"
        game1 = GameFactory(name="Catan")
        GameFactory(name="CosInnego")  # game2 = GameFactory(name="CosInnego")

        response = self.client.get(self.url, data={"name": "Catan"})

        self.assertEqual(200, response.status_code)
        self.assertEqual([game1], list(response.context["game_list"]))

    def test_return_games_with_fiter_game_type(self):
        gametype1 = GameTypeFactory(name="Strategia")
        gametype2 = GameTypeFactory(name="Strzelanka")
        game1 = GameFactory.create(game_type=[gametype1])  # game1 -  wpisywać nazwe klasy, informacjia o tym co to jest
        game2 = GameFactory.create()
        game2.game_type.set([gametype2])

        response = self.client.get(self.url, data={"game_type": gametype1.id})

        self.assertEqual(200, response.status_code)
        self.assertEqual([game1], list(response.context["game_list"]))
