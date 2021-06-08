from django.urls import path, include
from company.views import CompanyViewSet, BankAccountViewSet
from rest_framework import routers
from rest_framework_nested import routers


app_name='company'

router = routers.DefaultRouter()
router.register(r'', CompanyViewSet, basename='Company')

bank_router = routers.NestedDefaultRouter(
    router, r'', lookup="company"
)
bank_router.register(
    r"bank_accounts", BankAccountViewSet, basename='Company'
)

urlpatterns = [
    path('', include(router.urls)),
    path('',include(bank_router.urls))
]
