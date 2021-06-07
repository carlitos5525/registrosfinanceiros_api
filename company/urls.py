from django.urls import path, include
from company import views
from rest_framework import routers


app_name='company'

router = routers.DefaultRouter()
router.register(r'', views.CompanyViewSet, basename='Company')
urlpatterns = [
    path('', include(router.urls)),
]
