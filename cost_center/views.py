from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cost_center.serializers import CostCenterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cost_center.models import CostCenter


class CostCenterViewSet(ModelViewSet):
    serializer_class = CostCenterSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        query = CostCenter.objects.all()
        return query
