from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'turniej_app/index.html'