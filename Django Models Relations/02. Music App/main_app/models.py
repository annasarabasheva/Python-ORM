from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40, )


class Book(models.Model):
    title = models.CharField(max_length=40, )
    price = models.DecimalField(decimal_places=2, max_digits=5)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    songs = models.ManyToManyField(Song, related_name='artists')
