from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ark.models import Animal


class StartView(TemplateView):
    template_name = 'ark/start.html'


class AnimalListView(ListView):
    model = Animal
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Gender'] = Animal.Gender
        context['Gender'].do_not_call_in_templates = True
        return context


class AnimalDetailView(DetailView):
    # specify the model to use
    model = Animal
