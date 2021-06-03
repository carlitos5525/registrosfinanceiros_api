from django.urls import path, include
from finance_register import views
from rest_framework import routers



app_name='finance_register'

router = routers.DefaultRouter()
router.register(r'', views.RegisterViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
