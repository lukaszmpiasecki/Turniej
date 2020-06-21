from turniej_app.models.gracze_model import Gracze
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ListaGraczyView(ListView):
    model = Gracze
class CreateGraczeView(CreateView):
    model = Gracze
    fields = ['nazwa', 'turniej']
class UpdateGraczeView(UpdateView):
    model = Gracze
    fields = ['nazwa', 'turniej']
class DeleteGraczeView(DeleteView):
    model = Gracze
    success_url = reverse_lazy('lista_graczy')