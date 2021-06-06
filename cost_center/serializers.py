from rest_framework.serializers import ModelSerializer
from cost_center.models import CostCenter


class CostCenterSerializer(ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ('id', 'name', 'company_id')
