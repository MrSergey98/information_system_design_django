from django.forms import ModelForm

from firma.models import Client


class ClientForm(ModelForm):

    class Meta:
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