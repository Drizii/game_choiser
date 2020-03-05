from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = "__all__"  # TODO: test serializer  - REST API
