from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from finance_register.models import Ammount, Register
from finance_register.serializers import RegisterSerializer, AmmountSerializer
from rest_framework.decorators import action
from django.http import HttpResponse, Http404, response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class AmmountViewSet(ModelViewSet):
    serializer_class = AmmountSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        register_id = self.kwargs['register_pk']
        register = Register.objects.get(id=register_id)
        ammount_query = register.ammounts.all()
        return ammount_query

    def create(self, request, *args, **kwargs):
        register_id = self.kwargs['register_pk']
        register = Register.objects.get(id=register_id)
        ammount_data = request.data
        ammount_data['company_id'] = register.company_id
        ammount = Ammount.objects.create(**ammount_data)
        register.ammounts.add(ammount)
        register_serialized = RegisterSerializer(register)
        json = JSONRenderer().render(register_serialized.data)
        return HttpResponse(json)


class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        query = Register.objects.all()
        return query
