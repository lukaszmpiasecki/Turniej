from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class MyLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request, 'A user successfully logged out')
        return reverse_lazy('index')