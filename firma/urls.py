from django.contrib import admin
from django.urls import path, include

from firma.views import clients, ClientDetailsView, client_delete, ClientCreateView, ClientUpdateView

urlpatterns = [
    path('clients/', clients, name='clients'),
    path('details_client/<int:pk>/', ClientDetailsView.as_view(), name='details_client'),
    path('client_delete/<int:pk>/', client_delete, name='client_delete'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
]