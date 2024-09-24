import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


def show_highest_rated_art() -> str:
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"


def bulk_create_arts(first_art, second_art) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"

