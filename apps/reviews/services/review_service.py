from apps.reviews.models import Review


def create_review(user, product, rating, comment):
    review, created = Review.objects.update_or_create(
        user=user,
        product=product,
        defaults={
            "rating": rating,
            "comment": comment
        }
    )
    return review