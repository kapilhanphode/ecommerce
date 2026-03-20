from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.reviews.models import Review
from apps.reviews.serializers.review_serializer import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_id = self.request.query_params.get("product")
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)