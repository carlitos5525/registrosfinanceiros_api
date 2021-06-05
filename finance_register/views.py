from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from finance_register.models import Register
from finance_register.serializers import RegisterSerializer


class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        query = Register.objects.all()
        return query