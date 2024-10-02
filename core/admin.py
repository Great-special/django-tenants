from django.contrib import admin

# Register your models here.
from django_tenants.admin import TenantAdminMixin

from .models import Client, ClientDomain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'schema_name':('name',)}
    
    
admin.site.register(ClientDomain)