from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from movie.models import Cinema, Movie, Room, Showtime
from movie.serializers import (CinemaSerializer, MovieSerializer,
                               RoomSerializer, ShowtimeSerializer)
from user.permissions import IsAdminOrReadOnly


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(
        release__lte=datetime.now(), end_release__gt=datetime.now()
    )
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaList(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ShowtimeList(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["room__cinema", "movie", "start_time", "end_time"]


class ShowtimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminOrReadOnly,)
