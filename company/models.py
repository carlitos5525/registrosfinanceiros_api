from django.db import models
import uuid
from django.contrib.auth.models import User


class BankAccount(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    bank_name = models.CharField(max_length=50)
    bank_number = models.PositiveIntegerField()
    agency_number = models.CharField(max_length=10)
    account_number = models.CharField(max_length=12)
    account_digit = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Conta Bancária"
        verbose_name_plural = "Contas Bancárias"
    
    def __str__(self):
        return self.account_number


class Company(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    bank_accounts = models.ManyToManyField(BankAccount, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    
    def __str__(self):
        return self.user.username
