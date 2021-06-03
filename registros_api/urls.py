from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('finance-register/', include('finance_register.urls')),
    path('cost_center/', include('cost_center.urls')),
    path('company/', include('company.urls')),
]
