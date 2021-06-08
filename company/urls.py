from django.urls import path, include
from company import views
from rest_framework import routers
from rest_framework_nested import routers


app_name='company'

router = routers.DefaultRouter()
router.register(r'', views.CompanyViewSet, basename='Company')

bank_router = routers.NestedDefaultRouter(
    router, r'', lookup="id"
)
bank_router.register(
    r"bank_accounts", views.BankAccountViewSet, basename='Company'
)

urlpatterns = [
    path('', include(router.urls)),
    path('',include(bank_router.urls))
]
