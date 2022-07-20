from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    series=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})