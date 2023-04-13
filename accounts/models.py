from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


class UserAdmin(models.Model):
    pass
