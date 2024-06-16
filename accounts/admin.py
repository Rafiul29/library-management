from django.contrib import admin
from accounts.models import UserAddress,UserBankAccount

# Register your models here.

admin.site.register(UserBankAccount)
admin.site.register(UserAddress)