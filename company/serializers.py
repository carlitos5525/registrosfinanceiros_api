from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from company.models import BankAccount, Company, UserProfile
from django.contrib.auth.models import User


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'bank_accounts')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', "password" )


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ('user', 'company')

    def create(self, validated_data):
        user = validated_data['user']
        print(user)
        company_id = validated_data['company']
        created_user = User.objects.create_user(**user)
        user_profile = UserProfile.objects.create(user=created_user, company=company_id)
        return user_profile
