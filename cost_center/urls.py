from django.urls import path, include
from cost_center import views
from rest_framework import routers



app_name='cost_center'

router = routers.DefaultRouter()
router.register(r'', views.CostCenterViewSet, basename='CostCenter')
urlpatterns = [
    path('', include(router.urls)),
]
