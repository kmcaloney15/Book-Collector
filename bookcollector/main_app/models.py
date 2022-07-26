from django.db import models
from django.urls import reverse
from datetime import date

REVIEW = (
  ('A', 'Great'),
  ('B', 'Okay'),
  ('C', 'Not my favorite'),
)

class Fandom(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fandoms_detail', kwargs={'pk': self.id})


# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    series=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    fandom = models.ManyToManyField(Fandom)

    def __str__(self):
        return self.name

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})


class Review(models.Model):
  date = models.DateField('Review Date')
  review = models.CharField(
    'Review',
    max_length=1,
    choices=REVIEW,
    default=REVIEW[0][0]
  )
  # create a book_id column in the db
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_review_display()} on {self.date}"

  class Meta:
    ordering = ['-date']