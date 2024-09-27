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


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Review(models.Model):
    description = models.TextField(max_length=200, )
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name="reviews")


class Driver(models.Model):
    first_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50, )


class DrivingLicense(models.Model):
    license_number = models.CharField(max_length=10, unique=True, )
    issue_date = models.DateField()
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, )
