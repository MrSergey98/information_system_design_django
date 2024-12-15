from django.contrib import admin
from django.urls import path, include

from firma.views import main_page, clients, details_client, client_delete, ClientCreateView, ClientUpdateView

urlpatterns = [
    path('', main_page, name='main_page'),
    path('clients/', clients, name='clients'),
    path('details_client/<int:pk>/', details_client, name='details_client'),
    path('client_delete/<int:pk>/', client_delete, name='client_delete'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
]