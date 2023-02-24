from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('Date Added')

class Bets(models.Model):
    bet_name = models.CharField(max_length = 50)
    sport = models.CharField(max_length = 20)
    odds = models.IntegerField()


