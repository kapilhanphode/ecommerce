from django.db import models
from apps.core.models import BaseModel
from django.conf import settings


class Cart(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    session_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)
