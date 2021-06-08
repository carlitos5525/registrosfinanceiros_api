from django.urls import path, include
from company.views import CompanyViewSet, BankAccountViewSet, UserProfileViewSet
from rest_framework import routers
from rest_framework_nested import routers


app_name='company'

router = routers.DefaultRouter()
router.register(r'', CompanyViewSet, basename='Company')

company_router = routers.NestedDefaultRouter(
    router, r'', lookup="company"
)
company_router.register(
    r"bank_accounts", BankAccountViewSet, basename='Company'
)

company_router.register(
    r'users', UserProfileViewSet, basename='UserProfile'
)

urlpatterns = [
    path('', include(router.urls)),
    path('',include(company_router.urls)),
]
