from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Client(models.Model):
    """Модель клиента"""

    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = models.CharField(
        max_length=12,
        verbose_name='Телефонный номер',
        validators=[
            RegexValidator(
                regex='^((\+7)|8)9\d{9}$',
                message='Номер телефона должен начинаться с 8 или +7, далее иметь 9 цифр'
            )
        ]
    )
    firstname = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    fathers_name = models.CharField(verbose_name='Отчество', max_length=50, blank=True, null=True)
    pasport = models.CharField(
        verbose_name='Паспорт',
        max_length=15,
        validators=[
            RegexValidator(
                regex='^\d{6} \d{4}$',
                code='Паспорт должен быть в формате "<6_цифр><пробел><4_цифры>"'
            )
        ]
    )
    balance = models.FloatField(verbose_name='Баланс', default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.email} {self.surname} {self.firstname}'
