from django.db import models


class EventRegistration(models.Model):
    event_name = models.CharField(max_length=60,)
    participant_name = models.CharField(max_length=50,)
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.participant_name} - {self.event_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100,)
    director = models.CharField(max_length=100,)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50,)

    def __str__(self):
        return f'Movie "{self.title}" by {self.director}'


class Student(models.Model):
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10,)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"