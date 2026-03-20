from apps.reviews.models import Review
from django.db.models import Avg


def get_product_reviews(product):
    return Review.objects.filter(product=product)


def get_product_rating(product):
    return Review.objects.filter(product=product).aggregate(avg=Avg("rating"))
