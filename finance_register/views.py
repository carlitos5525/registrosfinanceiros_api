from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from finance_register.models import Register
from finance_register.serializers import RegisterSerializer


class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
