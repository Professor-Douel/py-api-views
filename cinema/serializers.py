from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.Serializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"
