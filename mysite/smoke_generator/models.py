import uuid

from django.db import models


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_txt = models.CharField(max_length=200)
    ingredients_txt = models.TextField()
    image_img = models.ImageField()
    description_txt = models.TextField()

    def __str__(self):
        return self.title