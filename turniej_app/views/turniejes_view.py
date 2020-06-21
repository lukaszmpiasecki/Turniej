from turniej_app.models.turnieje_model import Turnieje
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ListaTurniejowView(ListView):
    model = Turnieje
class CreateTurniejeView(CreateView):
    model = Turnieje
    fields = ['nazwa', 'czas_rozpoczecia', 'max_graczy']
class UpdateTurniejeView(UpdateView):
    model = Turnieje
    fields = ['nazwa', 'czas_rozpoczecia', 'max_graczy']
class DeleteTurniejeView(DeleteView):
    model = Turnieje
    success_url = reverse_lazy('lista_turniejow')