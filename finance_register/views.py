from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from finance_register.models import Ammount, Register
from finance_register.serializers import RegisterSerializer, AmmountSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        query = Register.objects.all()
        return query

    @action(methods=['put'], detail=True)
    def update_ammount(self, request, pk):
        ammount_data = request.data['ammount']
        register = Register.objects.get(id=pk)
        ammount_id = ammount_data['id']
        ammount = Ammount.objects.get(id=ammount_id)
        for attr, value in ammount_data.items():
            setattr(ammount, attr, value)
        ammount.save()
        ammount_serialized = AmmountSerializer(ammount)
        json = JSONRenderer().render(ammount_serialized.data)
        return HttpResponse(json)

    @action(methods=['post'], detail=True)
    def create_ammount(self, request, pk):
        ammount_data = request.data
        register = Register.objects.get(id=pk)
        ammount_data['company_id'] = register.company_id
        ammount = Ammount.objects.create(**ammount_data)
        register.ammounts.add(ammount)
        register_serialized = RegisterSerializer(register)
        json = JSONRenderer().render(register_serialized.data)
        return HttpResponse(json)

