from django.urls import path

from purchases.views import (
    VoucherListView,
    purchases_main_page,
    VoucherUpdateView,
    VoucherDetailsView,
    VoucherDeleteView,
    VoucherCreateView,
    VoucherOfferListView,
    VoucherOfferCreateView,
    VoucherOfferDetailsView,
    VoucherOfferUpdateView,
    VoucherOfferDeleteView, buy_voucher_offer,
)

urlpatterns = [
    path('', purchases_main_page, name='purchases_main_page'),
    path('vouchers/', VoucherListView.as_view(), name='vouchers'),
    path('voucher_create/', VoucherCreateView.as_view(), name='voucher_create'),
    path('voucher_details/<int:pk>/', VoucherDetailsView.as_view(), name='voucher_details'),
    path('voucher_update/<int:pk>/', VoucherUpdateView.as_view(), name='voucher_update'),
    path('voucher_delete/<int:pk>/', VoucherDeleteView.as_view(), name='voucher_delete'),
    path('voucher_offers/', VoucherOfferListView.as_view(), name='voucher_offers'),
    path('voucher_offer_create/', VoucherOfferCreateView.as_view(), name='voucher_offer_create'),
    path('voucher_offer_details/<uuid:pk>/', VoucherOfferDetailsView.as_view(), name='voucher_offer_details'),
    path('voucher_offer_update/<uuid:pk>/', VoucherOfferUpdateView.as_view(), name='voucher_offer_update'),
    path('voucher_offer_delete/<uuid:pk>/', VoucherOfferDeleteView.as_view(), name='voucher_offer_delete'),
    path('buy_voucher_offer/<uuid:pk>/', buy_voucher_offer, name='buy_voucher_offer'),
]