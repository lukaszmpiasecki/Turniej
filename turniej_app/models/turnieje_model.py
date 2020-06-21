from django.db import models
from django.urls import reverse


class Turnieje(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    czas_rozpoczecia = models.DateTimeField()
    max_graczy = models.IntegerField()

    def get_absolute_url(self):
        return reverse('lista_turniejow')
