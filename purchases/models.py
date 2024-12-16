from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from firma.models import Client


class Voucher(models.Model):
    """Модель путевки"""

    place = models.CharField(verbose_name='Место', max_length=100)
    date = models.DateTimeField(verbose_name='Дата')
    duration = models.FloatField(verbose_name='Длительность (в часах)', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Путевка'
        verbose_name_plural = 'Путевки'

    def __str__(self):
        return f'Путевка в {self.place} на {self.date}'


class VoucherOffer(models.Model):
    """Модель предложения путевки"""

    class VoucherOfferChoices:
        PAYED = 'payed'
        CLOSED = 'closed'
        OPEN = 'open'

        CHOICES = [
            (PAYED, 'Оплачено'),
            (CLOSED, 'Закрыто'),
            (OPEN, 'Открыто'),
        ]

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, models.SET_NULL, verbose_name='Клиент', blank=True, null=True, related_name='voucher_offers')
    voucher = models.ForeignKey(Voucher, models.SET_NULL, verbose_name='Путевка', null=True, related_name='voucher_offers')
    price = models.FloatField(verbose_name='Цена', validators=[MinValueValidator(0)])
    discount = models.IntegerField(verbose_name='Скидка', default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.CharField(choices=VoucherOfferChoices.CHOICES, max_length=20)

    class Meta:
        verbose_name = 'Предложение путевки'
        verbose_name_plural = 'Предложения путевок'

    def __str__(self):
        return f'Предложение путевки в {self.voucher.place} для {self.client}'