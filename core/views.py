from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h1>Public Index</h1>")
    
    return render(request, 'base_subdomain_nav.html')