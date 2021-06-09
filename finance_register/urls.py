from django.urls import path, include
from finance_register import views
from rest_framework import routers
from rest_framework_nested import routers


app_name='finance_register'

router = routers.DefaultRouter()
router.register(r'', views.RegisterViewSet, basename='Register')

register_router = routers.NestedDefaultRouter(
    router, r'', lookup='register'
)
register_router.register(
    r'ammounts', views.AmmountViewSet, basename='Ammount'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(register_router.urls))
]
