from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cost_center.serializers import CostCenterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cost_center.models import CostCenter
from company.models import UserProfile


class CostCenterViewSet(ModelViewSet):
    serializer_class = CostCenterSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)
        company_id = user_profile.company
        query = CostCenter.objects.filter(company_id=company_id)
        return query
        return query
