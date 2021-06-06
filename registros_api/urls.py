from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('finance-register/', include('finance_register.urls')),
    path('api-token-auth/', obtain_auth_token)
]
