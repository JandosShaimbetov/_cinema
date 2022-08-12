from django.contrib import admin

from movie.models import Cinema, Movie, Showtime

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Showtime)
