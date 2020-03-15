import factory
from main.models import Game, GameType



class GameTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"GameType_{n}")
    description = factory.Sequence(lambda n: f"GameType_description_{n}")

    class Meta:
        model = GameType


class GameFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Game_{n}")

    @factory.post_generation
    def game_type(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for game_type in extracted:
                self.game_type.add(game_type)


    class Meta:
        model = Game