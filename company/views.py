from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from company.serializers import BankAccountSerializer, CompanySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from company.models import BankAccount, Company
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


class BankAccountViewSet(ModelViewSet):
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        print(self.kwargs)
        company_id = self.kwargs["id_pk"]
        company = Company.objects.get(id=company_id)
        query = company.bank_accounts.all()
        return query


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['post', 'put', 'delete']
