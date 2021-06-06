from rest_framework import fields
from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from finance_register.models import Register
from finance_register.models import Ammount
from cost_center.serializers import CostCenterSerializer


class AmmountSerializer(ModelSerializer):
    cost_center_id = CostCenterSerializer()

    class Meta:
        model = Ammount
        fields = ('id', 'name', 'value', 'type', 'cost_center_id')

class RegisterSerializer(ModelSerializer):
    ammounts = AmmountSerializer(many=True)

    class Meta:
        model = Register
        fields ='__all__'

    def create_ammount(self, ammounts, register):
        for ammount in ammounts:
            ammount['company_id'] = register.company_id
            a = Ammount.objects.create(**ammount)
            register.ammounts.add(a)
    
    def create(self, validated_data):
        ammounts = validated_data['ammounts']
        del validated_data['ammounts']
        register = Register.objects.create(**validated_data)
        self.create_ammount(ammounts, register)
        register.save()
        return register

    def update(self, instance, validated_data):
        register = instance
        del validated_data['ammounts']
        for attr, value in validated_data.items():
            setattr(register, attr, value)
        register.save()
        return register
