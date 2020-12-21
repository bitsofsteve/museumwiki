from django.db import models


class Wiki(models.Model):
    name = models.CharField(max_length=255)
    established = models.CharField(max_length=4)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    collection_size = models.CharField(max_length=255)
    visitors = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
