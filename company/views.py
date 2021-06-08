from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import ModelViewSet
from company.serializers import BankAccountSerializer, CompanySerializer, UserProfileSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from company.models import BankAccount, Company, UserProfile
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


class BankAccountViewSet(ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        print(self.kwargs)
        company_id = self.kwargs["company_pk"]
        company = Company.objects.get(id=company_id)
        query = company.bank_accounts.all()
        return query

    def create(self, request, *args, **kwargs):
        bank_account_data = request.data
        bank_account = BankAccount.objects.create(**bank_account_data)
        company = get_object_or_404(Company, id=self.kwargs["company_pk"])
        company.bank_accounts.add(bank_account)
        bank_account_serialized = BankAccountSerializer(bank_account)
        json = JSONRenderer().render(bank_account_serialized.data)
        return HttpResponse(json)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        response = HttpResponse()
        response.status_code = 405
        return response


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        print(self.kwargs)
        company_id = self.kwargs["company_pk"]
        query = UserProfile.objects.filter(company=company_id)
        return query
