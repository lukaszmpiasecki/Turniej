from django.db import models
from django.urls import reverse
from turniej_app.models.turnieje_model import Turnieje


class Gracze(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    turniej = models.ForeignKey(Turnieje, blank=True, null=True, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('lista_graczy')
