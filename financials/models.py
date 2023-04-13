from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    ticker_symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name
