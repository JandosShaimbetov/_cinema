from django.db import models
from django.utils import timezone


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    release = models.DateField(default=timezone.now)
    end_release = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=200)
    cinema = models.ForeignKey(Cinema, related_name="cinema", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.movie} in {self.room} at {self.start_time}"
