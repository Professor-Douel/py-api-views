from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "description", "duration"]


class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class CinemaHallSerializer(serializers.Serializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "row", "seats_in_row"]
