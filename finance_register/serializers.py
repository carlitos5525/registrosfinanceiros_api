from rest_framework import fields
from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from finance_register.models import Register
from finance_register.models import Ammount


class AmmountSerializer(ModelSerializer):
    class Meta:
        model = Ammount
        fields = ('name', 'value', 'type', 'cost_center_id')

class RegisterSerializer(ModelSerializer):
    ammounts = AmmountSerializer(many=True)
    class Meta:
        model = Register
        fields ='__all__'
