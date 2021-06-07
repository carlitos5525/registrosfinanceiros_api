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
    http_method_names = ['post', 'put', 'delete']

    @action(methods=['post'], detail=True)
    def create_bank_account(self, request, pk):
        bank_account_data = request.data['bank_account']
        bank_account = BankAccount.objects.create(**bank_account_data)
        company = get_object_or_404(Company, id=pk)
        company.bank_accounts.add(bank_account)
        company_serialized = CompanySerializer(company)
        json = JSONRenderer().render(company_serialized.data)
        return HttpResponse(json)

    @action(methods=['put'], detail=True)
    def update_bank_account(self, request, pk):
        bank_account_data = request.data['bank_account']
        bank_account_id = bank_account_data['id']
        bank_account = get_object_or_404(BankAccount, id=bank_account_id)
        company = get_object_or_404(Company, id=pk)
        company_bank_accounts = company.bank_accounts.all()
        if bank_account in company_bank_accounts:
            for attr, value in bank_account_data.items():
                setattr(bank_account, attr, value)
            bank_account.save()
            company_serialized = CompanySerializer(company)
            json = JSONRenderer().render(company_serialized.data)
            return HttpResponse(json)
        else:
            response = HttpResponse('The bank account is not related to the company')
            response.status_code = 404
            return response

    @action(methods=['delete'], detail=True)
    def delete_bank_account(self, request, pk):
        bank_account_id = request.data['id']
        bank_account = get_object_or_404(BankAccount, id=bank_account_id)
        company = get_object_or_404(Company, id=pk)
        company_bank_accounts = company.bank_accounts.all()
        if bank_account in company_bank_accounts:
            bank_account.delete()
            company_serialized = CompanySerializer(company)
            json = JSONRenderer().render(company_serialized.data)
            return HttpResponse(json)
        else:
            response = HttpResponse('The bank account is not related to the company')
            response.status_code = 404
            return response
