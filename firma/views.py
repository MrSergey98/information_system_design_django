from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from rest_framework import status

from django.views.generic.edit import CreateView, UpdateView

from firma.forms import ClientForm
from firma.models import Client


def clients(request):
    return render(request, 'firma/clients.html', {'clients': Client.objects.all()})


def details_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    context = {
        'view': 'client_new',
        'form': ClientForm(
            {
                'email': client.email,
                'firstname': client.firstname,
                'surname': client.surname,
                'fathers_name': client.fathers_name,
                'balance': client.balance,
                'phone_number': client.phone_number,
                'pasport': client.pasport,
            }
        ),
    }
    return render(request, 'firma/shablon_form.html', context)


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
