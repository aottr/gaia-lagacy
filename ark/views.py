from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ark.models import Animal


class StartView(TemplateView):
    template_name = 'ark/start.html'


class AnimalListView(ListView):
    model = Animal

    def get_queryset(self):
        context = Animal.objects.all()

        if self.request.GET.get('gender'):
            gender = self.request.GET.get('gender')
            context = context.filter(gender=gender)

        if self.request.GET.get('species'):
            species = self.request.GET.get('species')
            context = context.filter(species=species)

        order = self.request.GET.get('order', '-pk')
        return context.order_by(order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Gender'] = Animal.Gender
        context['Gender'].do_not_call_in_templates = True
        return context


class AnimalDetailView(DetailView):
    # specify the model to use
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Gender'] = Animal.Gender
        context['Gender'].do_not_call_in_templates = True
        return context
