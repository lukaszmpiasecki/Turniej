from django.contrib import admin

from turniej_app.models.gracze_model import Gracze
from turniej_app.models.turnieje_model import Turnieje


admin.site.register(Turnieje)

admin.site.register(Gracze)
