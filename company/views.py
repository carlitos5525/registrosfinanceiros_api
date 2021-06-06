from company.models import BankAccount
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from company.serializers import BankAccountSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from company.models import BankAccount


class BankAccountViewSet(ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        query = BankAccount.objects.all()
        return query
