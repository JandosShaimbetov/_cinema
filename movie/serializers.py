from rest_framework import serializers

from movie.models import Cinema, Movie, Showtime
from reservation.models import Room


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "description",
            "image",
            "release",
            "end_release",
        ]


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            "id",
            "name",
            "description",
            "address",
            "contact",
            "open_time",
            "close_time",
        ]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "cinema"]


class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = ["id", "room", "movie", "start_time", "end_time"]
