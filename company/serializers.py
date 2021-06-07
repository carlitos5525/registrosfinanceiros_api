from rest_framework.serializers import ModelSerializer
from company.models import BankAccount, Company


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    bank_accounts = BankAccountSerializer(many=True)
    
    class Meta:
        model = Company
        fields = ('id', 'name', 'bank_accounts')
