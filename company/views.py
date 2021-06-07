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



class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['post', 'put']

    @action(methods=['post'], detail=True)
    def create_bank_account(self, request, pk):
        bank_account_data = request.data['bank_account']
        bank_account = BankAccount.objects.create(**bank_account_data)
        company = get_object_or_404(Company, id=pk)
        company.bank_accounts.add(bank_account)
        company_serialized = CompanySerializer(company)
        json = JSONRenderer().render(company_serialized.data)
        return HttpResponse(json)


