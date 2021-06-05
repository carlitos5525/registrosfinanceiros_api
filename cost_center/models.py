from django.db import models
from company.models import Company
import uuid


class CostCenter(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Centro de Custo'
        verbose_name_plural = 'Centros de Custo'
    
    def __str__(self):
        return self.name
