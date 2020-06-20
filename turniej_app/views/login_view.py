from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    def get_success_url(self):
        messages.success(self.request, 'A user successfully logged in')
        return reverse_lazy('index')