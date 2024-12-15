from django.contrib import admin
from firma.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'surname', 'fathers_name')
    search_fields = ('email', 'firstname', 'surname', 'fathers_name')
