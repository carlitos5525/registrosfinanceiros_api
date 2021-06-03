from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from finance_register.models import Register


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'name', 'due_date', 'pay_date', 'status', 'payment_method')