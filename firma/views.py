from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from rest_framework import status

from django.views.generic.edit import CreateView, UpdateView

from firma.forms import ClientForm
from firma.models import Client


def clients(request):
    return render(request, 'firma/clients.html', {'clients': Client.objects.all()})

class ClientDetailsView(DetailView):
    template_name_suffix = '_form'
    model = Client
    fields = ClientForm.Meta.fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_ = context.get('object')
        context['view_name'] = 'details'
        form = ClientForm(instance=object_, initial={'email': object_.email})

        context['form'] = form
        return context


@require_POST
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return HttpResponse(status=status.HTTP_200_OK)


class ClientCreateView(CreateView):
    model = Client
    fields = (
        'email',
        'firstname',
        'surname',
        'fathers_name',
        'balance',
        'phone_number',
        'pasport',
    )

    def get_success_url(self):
        return reverse('clients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'create'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    fields = (
        'email',
        'firstname',
        'surname',
        'fathers_name',
        'balance',
        'phone_number',
        'pasport',
    )

    def get_success_url(self):
        return reverse('clients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'update'
        return context
