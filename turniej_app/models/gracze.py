from django.db import models

class Gracze(models.Model):
    nazwa = models.CharField(max_length=50, primary_key=True)
    czas_rozpoczecia = models.DateTimeField()
    max_graczy = models.IntegerField()
