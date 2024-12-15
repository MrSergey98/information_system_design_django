from django.contrib import admin

from purchases.models import Voucher, VoucherOffer


# Register your models here.

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    pass

@admin.register(VoucherOffer)
class VoucherOfferAdmin(admin.ModelAdmin):
    pass
