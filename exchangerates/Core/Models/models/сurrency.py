from django.db import models


class Currency(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.slug}"