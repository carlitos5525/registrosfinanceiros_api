from rest_framework.serializers import ModelSerializer
from company.models import BankAccount, Company


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'