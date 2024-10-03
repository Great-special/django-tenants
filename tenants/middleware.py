from django.conf import settings
from django.http import Http404
from django_tenants.middleware.main import TenantMainMiddleware

class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        host = request.get_host().lower()
        
        # Skip tenant processing for accounts and blog subdomains
        if host.startswith(('accounts.', 'blog.')):
            return None
            
        try:
            return super().process_request(request)
        except Http404:
            # Handle cases where the subdomain doesn't match a tenant
            if host.startswith(('www.', f'www.{settings.PARENT_HOST}')):
                # Handle main domain logic here
                return None
            raise