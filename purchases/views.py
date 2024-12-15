from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from rest_framework import status
from rest_framework.response import Response

from firma.views import clients
from purchases.forms import VoucherForm, VoucherOfferForm
from purchases.models import Voucher, VoucherOffer

VOUCHER_FIELDS = (
    'place',
    'date',
    'duration',
)
VOUCHER_OFFER_FIELDS = (
    'client',
    'voucher',
    'price',
    'discount',
    'status',
)

def purchases_main_page(request):
    return render(request, 'purchases/index.html')


class VoucherListView(ListView):
    template_name_suffix = '_list'
    model = Voucher
    fields = VOUCHER_FIELDS

class VoucherCreateView(CreateView):
    template_name_suffix = '_form'
    model = Voucher
    fields = VOUCHER_FIELDS

    def get_success_url(self):
        return reverse('vouchers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'create'
        return context


class VoucherUpdateView(UpdateView):
    template_name_suffix = '_form'
    model = Voucher
    fields = VOUCHER_FIELDS

    def get_success_url(self):
        return reverse('vouchers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'update'
        return context

class VoucherDetailsView(DetailView):
    template_name_suffix = '_form'
    model = Voucher
    fields = VOUCHER_FIELDS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_ = context.get('object')
        context['form'] = VoucherForm(
            {field: getattr(object_, field) for field in VOUCHER_FIELDS}
        )
        return context

class VoucherDeleteView(DeleteView):
    model = Voucher
    fields = VOUCHER_FIELDS
    def get_success_url(self):
        return reverse('vouchers')


class VoucherOfferListView(ListView):
    template_name_suffix = '_list'
    model = VoucherOffer
    fields = VOUCHER_OFFER_FIELDS

class VoucherOfferCreateView(CreateView):
    template_name_suffix = '_form'
    model = VoucherOffer
    fields = VOUCHER_OFFER_FIELDS

    def get_success_url(self):
        return reverse('voucher_offers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'create'
        return context


class VoucherOfferUpdateView(UpdateView):
    template_name_suffix = '_form'
    model = VoucherOffer
    fields = VOUCHER_OFFER_FIELDS

    def get_success_url(self):
        return reverse('voucher_offers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'update'
        return context

class VoucherOfferDetailsView(DetailView):
    template_name_suffix = '_form'
    model = VoucherOffer
    fields = VOUCHER_OFFER_FIELDS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_ = context.get('object')
        context['form'] = VoucherOfferForm(
            {field: getattr(object_, field) for field in VOUCHER_OFFER_FIELDS}
        )
        return context

class VoucherOfferDeleteView(DeleteView):
    model = VoucherOffer
    fields = VOUCHER_OFFER_FIELDS
    def get_success_url(self):
        return reverse('voucher_offers')

@require_POST
@transaction.atomic
def buy_voucher_offer(request, pk):
    voucher_offer: VoucherOffer = VoucherOffer.objects.get(pk=pk)
    voucher_offer.client.balance -= voucher_offer.price*(1-voucher_offer.discount/100)
    if voucher_offer.client.balance < 0:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    voucher_offer.client.save()
    voucher_offer.status = voucher_offer.VoucherOfferChoices.PAYED
    voucher_offer.save()
    return HttpResponse(status=status.HTTP_200_OK)
