from django.urls import path

from movie.views import (CinemaDetail, CinemaList, MovieDetail, MovieList,
                         ShowtimeDetail, ShowtimeList)

urlpatterns = [
    path("", MovieList.as_view(), name="movies"),
    path("<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
    path("cinema/", CinemaList.as_view(), name="cinemas"),
    path("cinema/<int:pk>/", CinemaDetail.as_view(), name="cinema-detail"),
    path("showtime/", ShowtimeList.as_view(), name="showtimes"),
    path("showtime/<int:pk>/", ShowtimeDetail.as_view(), name="showtime-detail"),
]
