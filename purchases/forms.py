from django.forms import ModelForm

from purchases.models import Voucher, VoucherOffer


class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = (
            'place',
            'date',
            'duration',
        )

class VoucherOfferForm(ModelForm):
    class Meta:
        model = VoucherOffer
        fields = (
            'client',
            'voucher',
            'price',
            'discount',
            'status',
        )
