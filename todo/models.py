from django.db import models


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
