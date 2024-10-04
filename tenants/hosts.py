from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', 'core.urls', name='www'),  # Main domain
    host(r'accounts', 'accounts.urls', name='accounts'),  # Accounts subdomain
    host(r'(?!accounts|www)\w+', 'tenants.urls', name='tenant'), # So this checks that the subdomain is NOT "accounts" or "blog"
)
