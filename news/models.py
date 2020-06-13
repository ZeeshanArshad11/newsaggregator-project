from django.db import models
from datetime import date

# Create your models here.
class Headline(models.Model):
  title = models.CharField(max_length=500, unique=True)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  date = models.DateField( blank=True, auto_now_add=True)

  def __str__(self):
    return self.title

class Category(models.Model):
    CHOICES = [
    ('1', 'Technology'),
    ('2', 'Health'),
    ('3', 'Sports'),
    ('4', 'International'),
    ('5', 'National'),
    ]
    headline = models.ManyToManyField(Headline)
    name = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.name
