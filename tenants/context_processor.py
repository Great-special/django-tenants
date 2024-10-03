# tenants/context_processors.py

from core.models import Client

def tenant_context(request):
    available_tenants = []
    
    # Only fetch tenants for staff users
    if hasattr(request, 'user') and request.user.is_authenticated and request.user.is_staff:
        available_tenants = Client.objects.select_related('domains').exclude(schema_name='public')
        # Convert to a list of dicts for easy template use
        available_tenants = [
            {
                'name': tenant.name,
                'domain_url': tenant.domains.first().domain
            }
            for tenant in available_tenants
        ]
    
    return {
        'available_tenants': available_tenants
    }