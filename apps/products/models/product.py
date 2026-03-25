from django.db import models
from django.utils.text import slugify
from django.conf import settings
from apps.core.models import BaseModel
from .category import Category


class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["created_by"]),
            models.Index(fields=["category"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
