from typing import TYPE_CHECKING
from django.db import models
import uuid


class Register(models.Model):
    STATUS_CHOICES = (
        ('LT', 'Late'),
        ('PD', 'Paid'),
        ('PR', 'Predicted')
    )

    PAYMENT_METHOD_CHOICES = (
        ('B', 'Boleto'),
        ('CD', 'Cartão de débito'),
        ('CC', 'Cartão de crédito'),
        ('TED', 'TED'),
        ('DOC', 'DOC'),
        ('PIX', 'PIX'),
        ('CHQ', 'Cheque'),
        ('DDA', 'DDA')
    )
    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    due_date = models.DateField()
    pay_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=2,choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=3, choices=PAYMENT_METHOD_CHOICES)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'


class Ammount(models.Model):
    TYPE_CHOICES = (
        ('F', 'Fixo'),
        ('V', 'Variavel')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True, choices=TYPE_CHOICES)
    finance_register = models.ForeignKey(Register, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'
