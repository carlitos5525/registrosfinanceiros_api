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
    pay_date = models.DateField()
    status = models.CharField(max_length=2,choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=3, choices=PAYMENT_METHOD_CHOICES)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    