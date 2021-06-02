from typing import TYPE_CHECKING
from django.db import models
from company.models import Company, BankAccount
from cost_center.models import CostCenter
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
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True, blank=True)

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
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    cost_center_id = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'
