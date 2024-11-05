import os
import django
from django.db.models import Q, Count, Avg
from django.utils import timezone


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""
    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)
    if search_name is not None and search_email is not None:
        query |= query_name & query_email
    elif search_name is not None:
        query |= query_name
    else:
        query |= query_email

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ""

    output = "\n".join(
        [f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}"
            for author in authors])
    return output


def get_top_publisher():
    top_publisher = Author.objects.annotate(num_articles=Count('articles')).filter(num_articles__gt=0).order_by('-num_articles', 'email').first()
    if top_publisher:
        return f"Top Author: {top_publisher.full_name} with {top_publisher.num_articles} published articles."
    else:
        return ""


def get_top_reviewer():
    author = Author.objects.annotate(num_reviews=Count('reviews')).filter(num_reviews__gt=0).order_by('-num_reviews', 'email').first()
    if author:
        return f"Top Reviewer: {author.full_name} with {author.num_reviews} published reviews."
    else:
        return ""


def get_latest_article():
    latest_article = Article.objects.order_by('-id').first()

    if latest_article:
        latest_article = Article.objects.order_by('-published_on').first()

        if latest_article:
            authors = latest_article.authors.all().order_by('full_name')
            author_names = ", ".join([author.full_name for author in authors])

            num_reviews = latest_article.reviews.count()
            avg_rating = latest_article.reviews.aggregate(Avg('rating'))['rating__avg']
            avg_rating = "{:.2f}".format(avg_rating) if avg_rating is not None else "0.00"

            return f"The latest article is: {latest_article.title}. Authors: {author_names}. Reviewed: {num_reviews} times. Average Rating: {avg_rating}."
        else:
            return ""


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(num_reviews=Count('reviews')).filter(num_reviews__gt=0).annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating', 'title').first()
    if top_rated_article:
        return f"The top-rated article is: {top_rated_article.title}, with an average rating of {top_rated_article.avg_rating:.2f}, reviewed {top_rated_article.num_reviews} times."
    else:
        return ""


def ban_author(email=None):
    if email is None or not Author.objects.exists():
        return "No authors banned."
    author = Author.objects.filter(email__exact=email).first()
    if author:
        num_reviews = author.reviews.count()
        author.is_banned = True
        author.save()
        author.reviews.all().delete()
        return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."

    else:
        return "No authors banned."


print(get_latest_article())