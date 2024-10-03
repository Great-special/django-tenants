from django_hosts import patterns, host

host_patterns = patterns('',
    host('www', 'core.urls', name='www'),  # Main domain
    host('accounts', 'accounts.urls', name='accounts'),  # Accounts subdomain
    host(r'(?!accounts|blog)\w+', 'tenants.urls', name='tenant'), # So this checks that the subdomain is NOT "accounts" or "blog"
)
