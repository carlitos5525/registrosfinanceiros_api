from django.contrib import admin
from company.models import Company, BankAccount, UserProfile


admin.site.register(Company)
admin.site.register(BankAccount)
admin.site.register(UserProfile)
